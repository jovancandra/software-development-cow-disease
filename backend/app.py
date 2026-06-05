from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from skimage.feature import hog
import joblib
import os
import time

# =========================
# INISIALISASI FLASK Ebim
# =========================

app = Flask(__name__)

# Folder upload
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Membuat folder uploads otomatis
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Format file yang diizinkan
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# LOAD MODEL MACHINE LEARNING
model = joblib.load('model.pkl')

# =========================
# VALIDASI FORMAT FILE
# =========================

def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )

# =========================
# EKSTRAKSI FITUR HOG
# =========================

def extract_features(image_path):

    img = cv2.imread(image_path)

    img = cv2.resize(img, (256, 256))

    img = cv2.GaussianBlur(img, (5, 5), 0)

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

            # SIMPAN FILE BARU
            filepath = os.path.join(
                app.config['UPLOAD_FOLDER'],
                file.filename
            )

            file.save(filepath)

            # EKSTRAKSI FITUR
            features = extract_features(filepath)

            # Ubah menjadi array numpy
            features = np.array(features).reshape(1, -1)

            # LOADING AI
            time.sleep(2)

            # Confidence
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
                f"Tingkat Keyakinan AI: "
                f"{confidence_percent}%"
            )

            # PREDIKSI AI
            result = model.predict(features)[0]

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

            # TAMPILKAN GAMBAR
            image_path = filepath

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
# API DIAGNOSIS
# =========================

@app.route('/diagnosis', methods=['POST'])
def diagnosis():

    file = request.files.get('image')

    if not file:

        return jsonify({
            "status": "error",
            "message": "Gambar tidak ditemukan"
        }), 400

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(filepath)

    features = extract_features(
        filepath
    )

    features = np.array(
        features
    ).reshape(1, -1)

    result = model.predict(
        features
    )[0]

    if result == 0:

        hasil = "Sapi Sehat"

    elif result == 1:

        hasil = (
            "Sapi Terindikasi "
            "Lumpy Skin Disease"
        )

    else:

        hasil = (
            "Bukan Sapi"
        )

    return jsonify({

        "status": "success",

        "hasil_diagnosis": hasil

    })

# =========================
# JALANKAN FLASK
# =========================

if __name__ == '__main__':
    app.run(debug=True)