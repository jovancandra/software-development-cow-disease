# 🐄 Sistem Deteksi Lumpy Skin Disease pada Sapi Berbasis Web

## 📌 Deskripsi Proyek

Aplikasi ini merupakan sistem berbasis web yang dirancang untuk membantu peternak sapi dalam melakukan deteksi dini penyakit **Lumpy Skin Disease (LSD)** menggunakan citra gambar sapi.

Sistem bekerja dengan cara menganalisis gambar yang diunggah oleh pengguna menggunakan metode **Machine Learning**, sehingga dapat memberikan hasil deteksi secara cepat dan mudah dipahami.

Aplikasi ini dapat digunakan tanpa proses login (**zero-authentication**) sehingga pengguna dapat langsung mengakses fitur deteksi.

---

## 🎯 Tujuan

- Membantu deteksi dini penyakit Lumpy Skin Disease pada sapi
- Memberikan informasi edukasi kepada peternak
- Mengurangi risiko keterlambatan penanganan penyakit ternak
- Menyediakan sistem deteksi berbasis Artificial Intelligence
- Mempermudah proses pemeriksaan awal kesehatan sapi

---

## 🚀 Fitur Utama

- Upload gambar sapi
- Deteksi otomatis menggunakan Machine Learning
- Hasil prediksi penyakit sapi
- Identifikasi gambar:
  - Sapi sehat
  - Sapi terindikasi Lumpy Skin Disease
  - Gambar non-sapi
- Validasi gambar non-sapi
- Tampilan website sederhana dan mudah digunakan
- Informasi edukasi penyakit Lumpy Skin Disease
- Rekomendasi penanganan awal

---

## 📊 Alur Sistem

1. Pengguna membuka website
2. Pengguna mengunggah gambar sapi
3. Frontend mengirim gambar ke backend
4. Backend menerima dan memproses gambar
5. Sistem melakukan preprocessing dan ekstraksi fitur citra
6. Model Machine Learning melakukan prediksi
7. Backend mengirim hasil prediksi ke frontend
8. Frontend menampilkan hasil deteksi dan informasi penanganan awal

---

## 🏗️ Arsitektur Sistem

### 1. Frontend

Frontend digunakan sebagai antarmuka pengguna untuk mengunggah gambar, menampilkan proses analisis, dan menampilkan hasil deteksi.

### 2. Backend

Backend menggunakan Flask API untuk menerima gambar dari frontend, memproses gambar, menjalankan model Machine Learning, dan mengirimkan hasil prediksi.

### 3. Machine Learning Model

Model Machine Learning digunakan untuk melakukan klasifikasi gambar. Model yang digunakan adalah **Decision Tree** dengan ekstraksi fitur citra menggunakan **HOG Feature Extraction**.

### 4. Dataset

Dataset digunakan untuk melatih model klasifikasi citra. Dataset terdiri dari gambar sapi sehat, sapi terkena Lumpy Skin Disease, dan gambar non-sapi.

Dataset tidak disimpan langsung di repository karena ukuran file yang besar. Link dataset tersedia pada folder `dataset/README.md`.

---

## 🛠️ Teknologi yang Digunakan

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Decision Tree
- HOG Feature Extraction

### Library Pendukung
- OpenCV
- NumPy
- Joblib
- scikit-image

---

## 📂 Struktur Folder

```text
software-development-cow-disease/
│
├── backend/
│   ├── app.py
│   ├── model.pkl
│   ├── train_model.py
│   ├── training_model.ipynb
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── WireframeUI/
│
├── dataset/
│   └── README.md
│
├── docs/
│   └── Proposal Software Development.docx
│
├── README.md
└── .gitignore
