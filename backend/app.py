from flask import Flask, render_template, request
import cv2
import numpy as np
from skimage.feature import hog
import joblib
import os
import time


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

# VALIDASI FORMAT FILE

def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# EKSTRAKSI FITUR HOG

def extract_features(image_path):

    # Membaca gambar
    img = cv2.imread(image_path)

    # Resize gambar lebih besar
    img = cv2.resize(img, (256, 256))

    # Mengurangi noise gambar
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # Ubah ke grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ekstraksi fitur HOG
    features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(16, 16),
        cells_per_block=(2, 2),
        block_norm='L2-Hys'
    )

    return features

# HALAMAN UTAMA
@app.route('/', methods=['GET', 'POST'])
def index():

    prediction = None
    image_path = None
    error = None
    confidence_text = None

    # Jika tombol submit ditekan
    if request.method == 'POST':

        # Ambil file dari form
        file = request.files['image']

        # Jika file kosong
        if file.filename == '':

            error = "Silakan pilih gambar terlebih dahulu."

        # Jika format file benar
        elif file and allowed_file(file.filename):

            # HAPUS FILE LAMA
            for old_file in os.listdir(UPLOAD_FOLDER):

                old_path = os.path.join(
                    UPLOAD_FOLDER,
                    old_file
                )

                try:
                    os.remove(old_path)

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
            # CONFIDENCE AI
            probabilities = model.predict_proba(features)[0]

            confidence = max(probabilities)

            confidence_percent = round(confidence * 100, 2)

            confidence_text = (
                f"Tingkat Keyakinan AI : "
                f"{confidence_percent}%"
            )

            # PREDIKSI AI
            result = model.predict(features)[0]

            # HASIL PREDIKSI

            # Jika AI terlalu ragu
            if confidence < 0.65:

                prediction = (
                    "Gambar tidak dapat "
                    "dikenali dengan jelas"
                )

            else:

                # Sapi sehat
                if result == 0:

                    prediction = "Sapi Sehat"

                # Sapi lumpy
                elif result == 1:

                    prediction = (
                        "Sapi Terindikasi "
                        "Lumpy Skin Disease"
                    )

                # Bukan sapi
                else:

                    prediction = (
                        "Gambar bukan sapi "
                        "atau tidak dikenali"
                    )

            # TAMPILKAN GAMBAR

            image_path = filepath

 
        # FORMAT FILE SALAH
        else:

            error = (
                "Format file tidak didukung! "
                "Gunakan JPG, JPEG, atau PNG."
            )

    # RENDER WEBSITE
    return render_template(
        'index.html',
        prediction=prediction,
        image_path=image_path,
        error=error,
        confidence_text=confidence_text
    )

# MENJALANKAN FLASK
if __name__ == '__main__':

    app.run(debug=True)