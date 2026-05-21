# 🐄 Software Development: Sistem Deteksi Penyakit Lumpy Pada Sapi

## 📌 Deskripsi Proyek

Aplikasi ini merupakan sistem berbasis web yang dirancang untuk membantu peternak sapi dalam melakukan deteksi dini penyakit Lumpy Skin Disease (LSD) menggunakan citra gambar sapi.

Sistem bekerja dengan cara menganalisis gambar yang diupload oleh pengguna menggunakan metode Machine Learning sehingga dapat memberikan hasil deteksi secara cepat dan mudah dipahami.

Aplikasi ini dapat digunakan tanpa proses login (zero-authentication) sehingga lebih cepat diakses oleh peternak di lapangan.

---

# 🎯 Tujuan

- Membantu deteksi dini penyakit Lumpy Skin Disease pada sapi
- Memberikan edukasi kepada peternak
- Mengurangi risiko penyebaran penyakit ternak
- Menyediakan sistem deteksi berbasis Artificial Intelligence
- Mempermudah proses pemeriksaan awal kesehatan sapi

---

# 🚀 Fitur Utama

- Upload gambar sapi
- Deteksi otomatis menggunakan Artificial Intelligence
- Hasil prediksi penyakit sapi
- Identifikasi sapi sehat / terindikasi Lumpy
- Validasi gambar non-sapi
- Tampilan website responsif dan mudah digunakan
- Loading proses analisis AI
- Informasi edukasi penyakit Lumpy

---

# 📊 Alur Sistem

1. Pengguna membuka website
2. Pengguna mengupload gambar sapi
3. Sistem memproses gambar menggunakan Machine Learning
4. Sistem melakukan ekstraksi fitur citra
5. AI melakukan prediksi penyakit
6. Hasil deteksi ditampilkan kepada pengguna
7. Sistem memberikan informasi penanganan dan pencegahan

---

# 🏗️ Arsitektur Sistem

## 1. Frontend (User Interface)

Menampilkan tampilan website untuk upload gambar, hasil deteksi, dan informasi edukasi penyakit.

## 2. Backend (Flask API)

Memproses gambar upload pengguna dan menjalankan model Machine Learning untuk prediksi penyakit.

## 3. Machine Learning Model

Model Decision Tree digunakan untuk melakukan klasifikasi gambar sapi sehat, sapi terindikasi Lumpy, dan gambar non-sapi.

## 4. Dataset

Dataset berisi gambar:

- Sapi sehat
- Sapi terkena Lumpy Skin Disease
- Gambar non-sapi

---

# 🛠️ Teknologi yang Digunakan

## Frontend

- HTML
- CSS
- JavaScript

## Backend

- Python Flask

## Machine Learning

- Scikit-learn
- Decision Tree
- HOG Feature Extraction

## Library Pendukung

- OpenCV
- NumPy
- Joblib
- scikit-image

---

# 📂 Struktur Folder

```plaintext
project_lumpy/
│
├── dataset/
│   ├── healthycows/
│   ├── lumpycows/
│   └── noncows/
│
├── static/
│   ├── uploads/
│   ├── style.css
│   └── sapifoto.jpeg
│
├── templates/
│   └── index.html
│
├── app.py
├── model.pkl
├── training_model.ipynb
├── train_model.py
│
└── README.md