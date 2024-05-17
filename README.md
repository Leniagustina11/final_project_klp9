# Flower Classification Project

## Anggota Tim
1. **Devi Anggraini** (2108107010008)
2. **Leni Agustina** (2108107010070)
3. **Afifah Nibras** (2108107010097)
4. **Nabila Quratul Annisa** (2108107010010)

   
## Deskripsi Proyek
Proyek ini bertujuan untuk mengklasifikasikan gambar bunga menggunakan model pembelajaran mendalam (deep learning) yang dibangun dengan TensorFlow dan disajikan melalui API yang dibangun dengan FastAPI. Model ini dilatih untuk mengenali lima jenis bunga: **Daisy**, **Dandelion**, **Rose**, **Sunflower**, dan **Tulip**. Dengan menggunakan dataset gambar bunga. Dataset yang di gunakan di ambil dari situs roboflow. Model ini dapat memprediksi jenis bunga dari gambar yang diberikan oleh pengguna.

## Instruksi Penerapan
Berikut adalah langkah-langkah untuk menerapkan dan menjalankan proyek klasifikasi gambar bunga ini:

### Prasyarat
Pastikan Anda telah menginstal paket-paket berikut:
- Python 3.x
- TensorFlow
- NumPy
- FastAPI
- Uvicorn

Anda dapat menginstal paket-paket tersebut menggunakan pip:
```sh
pip install tensorflow numpy fastapi uvicorn
```

### Langkah-langkah
1. **Kloning Repositori**:
   Kloning repositori proyek ini ke komputer Anda.
   ```sh
   git clone https://github.com/username/flower-classification.git
   cd flower-classification
   ```

2. **Persiapkan Model**:
   Pastikan Anda telah memiliki model terlatih yang disimpan dalam format `.h5`. Jika Anda belum memiliki model, Anda bisa melatihnya menggunakan dataset bunga dan menyimpan model tersebut.

3. **Menjalankan Kode dari GitHub**:
   Untuk menjalankan proyek ini dari GitHub, ikuti langkah-langkah berikut:
   - Kloning repositori dan pindah ke direktori proyek seperti dijelaskan di atas.
   - Pastikan semua prasyarat sudah diinstal.
   - Jalankan API dengan perintah:
     ```sh
     uvicorn app:app --reload
     ```
   - API akan berjalan di `http://127.0.0.1:8000`.
