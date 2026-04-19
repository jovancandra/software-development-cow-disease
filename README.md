# 🐄 Software Development: Sistem Diagnosa Scabies pada Sapi

## 📌 Deskripsi Proyek
Aplikasi ini merupakan sistem berbasis web yang dirancang untuk membantu peternak sapi dalam melakukan diagnosa dini penyakit scabies (kudis) berdasarkan gejala yang dipilih pengguna.

Sistem menggunakan pendekatan machine learning untuk memberikan hasil diagnosa secara cepat dan membantu pengguna memperoleh rekomendasi penanganan awal.

Aplikasi ini dapat digunakan tanpa proses login (zero-authentication) sehingga lebih cepat diakses, terutama di lingkungan peternakan dengan keterbatasan akses.

---

## 🎯 Tujuan
- Membantu deteksi dini penyakit scabies pada sapi  
- Memberikan informasi dan edukasi kepada peternak  
- Mengurangi risiko penyebaran penyakit ternak  
- Menyediakan sistem diagnosa yang mudah digunakan  

---

## 🚀 Fitur Utama
- Input gejala penyakit sapi  
- Proses diagnosa otomatis berbasis machine learning  
- Hasil diagnosa (positif / negatif scabies)  
- Rekomendasi penanganan  
- Tanpa login (akses cepat)  

---

## 📊 Alur Sistem
1. Pengguna membuka website  
2. Pengguna memilih gejala yang dialami sapi  
3. Sistem memproses data menggunakan model machine learning  
4. Hasil diagnosa ditampilkan  
5. Sistem memberikan rekomendasi penanganan  

---

## 🏗️ Arsitektur Sistem

### 1. Frontend (User Interface)
Menampilkan antarmuka pengguna untuk input gejala dan hasil diagnosa  

### 2. Backend (API / Logic)
Memproses data gejala dan menjalankan logika diagnosa  

### 3. Database (Knowledge Base)
Menyimpan data gejala, penyakit, dan solusi  

---

## 🛠️ Teknologi yang Digunakan
*(Dapat disesuaikan selama pengembangan)*

- **Frontend**: HTML, CSS, JavaScript / React  
- **Backend**: Node.js / Laravel (menyesuaikan)  
- **Machine Learning**: Python (scikit-learn)  
- **Database**: MySQL / MongoDB  

---

## 📂 Struktur Folder

project-root/
│
├── frontend/ # Tampilan UI
├── backend/ # API dan logic sistem
├── model/ # Model machine learning
├── docs/ # Dokumentasi proyek
├── README.md
└── .gitignore


---

## 👥 Tim Pengembang
- **Project Manager**: Jovan Candra Winata  
- **Frontend Developer**: Moch. Hasbi Latif  
- **Backend Developer**: Ferdinas Ebim  

---

## 📝 Status Proyek
🚧 Dalam tahap pengembangan  

---

## 📄 Catatan
Aplikasi ini tidak menggantikan peran dokter hewan, melainkan sebagai alat bantu untuk diagnosa awal pada peternak.