from flask import Flask, render_template, request
import cv2
import numpy as np
from skimage.feature import hog
import joblib
import os
import time

# =========================
# PATH PROJECT
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIR = os.path.join(
    BASE_DIR,
    '..',
    'frontend',
    'templates'
)
STATIC_DIR = os.path.join(
    BASE_DIR,
    '..',
    'frontend',
    'static'
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    'static',
    'uploads'
)

# =========================
# FLASK APP
# =========================

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Buat folder uploads otomatis
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# FORMAT FILE
# =========================

ALLOWED_EXTENSIONS = {
    'png',
    'jpg',
    'jpeg'
}

# =========================
# LOAD MODEL
# =========================

MODEL_PATH = os.path.join(
    BASE_DIR,
    'model.pkl'
)

model = joblib.load(MODEL_PATH)

# =========================
# VALIDASI FILE
# =========================

def allowed_file(filename):

    return (
        '.' in filename
        and
        filename.rsplit('.', 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )

# =========================
# EKSTRAKSI HOG
# =========================

def extract_features(image_path):

    img = cv2.imread(image_path)

    if img is None:
        raise ValueError(
            f"Gagal membaca gambar: {image_path}"
        )

    img = cv2.resize(
        img,
        (256, 256)
    )

    img = cv2.GaussianBlur(
        img,
        (5, 5),
        0
    )

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(16, 16),
        cells_per_block=(2, 2),
        block_norm='L2-Hys'
    )

    return features

# =========================
# HALAMAN UTAMA
# =========================

@app.route('/', methods=['GET', 'POST'])
def index():

    prediction = None
    image_path = None
    error = None
    confidence_text = None

    if request.method == 'POST':

        if 'image' not in request.files:

            error = "File tidak ditemukan"

            return render_template(
                'index.html',
                prediction=prediction,
                image_path=image_path,
                error=error,
                confidence_text=confidence_text
            )

        file = request.files['image']

        if file.filename == '':

            error = (
                "Silakan pilih gambar terlebih dahulu."
            )

        elif file and allowed_file(file.filename):

            # Hapus file lama
            for old_file in os.listdir(
                UPLOAD_FOLDER
            ):

                try:

                    os.remove(
                        os.path.join(
                            UPLOAD_FOLDER,
                            old_file
                        )
                    )

                except:
                    pass

            filepath = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(filepath)

            features = extract_features(
                filepath
            )

            features = np.array(
                features
            ).reshape(1, -1)

            time.sleep(2)

            probabilities = model.predict_proba(
                features
            )[0]

            confidence = max(
                probabilities
            )

            confidence_percent = round(
                confidence * 100,
                2
            )

            confidence_text = (
                f"Tingkat Keyakinan AI : "
                f"{confidence_percent}%"
            )

            result = model.predict(
                features
            )[0]

            if confidence < 0.65:

                prediction = (
                    "Gambar tidak dapat "
                    "dikenali dengan jelas"
                )

            else:

                if result == 0:

                    prediction = (
                        "Sapi Sehat"
                    )

                elif result == 1:

                    prediction = (
                        "Sapi Terindikasi "
                        "Lumpy Skin Disease"
                    )

                else:

                    prediction = (
                        "Gambar bukan sapi "
                        "atau tidak dikenali"
                    )

            image_path = os.path.join(
                'static',
                'uploads',
                file.filename
            )

        else:

            error = (
                "Format file tidak didukung. "
                "Gunakan JPG, JPEG, atau PNG."
            )

    return render_template(
        'index.html',
        prediction=prediction,
        image_path=image_path,
        error=error,
        confidence_text=confidence_text
    )

# =========================
# JALANKAN FLASK
# =========================

if __name__ == '__main__':

    print("Template Folder:")
    print(TEMPLATE_DIR)

    print("Model Path:")
    print(MODEL_PATH)

    app.run(debug=True)