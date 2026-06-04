# -Kelompok-6-_ProjekDeteksiKaganga-
Proyek ini merupakan sistem deteksi objek untuk mengenali aksara Kaganga menggunakan model YOLOv11 dari library Ultralytics YOLO. Model dilatih menggunakan dataset dari Roboflow melalui Google Colab, kemudian hasil model digunakan untuk melakukan deteksi pada gambar secara lokal menggunakan Python.

# Fitur:
- Deteksi aksara Kaganga pada gambar
- Menggunakan model hasil training sendiri (best.pt)
- Menampilkan hasil deteksi secara langsung
- Menggunakan YOLOv11 untuk proses object detection

# Struktur Folder:
- ├── best.pt              # Model hasil training
- ├── gambar_test.jpg      # Gambar untuk diuji
- ├── main.py              # Program utama
- └── README.md

# Cara Menjalankan Program:
  1. install library yang dibutuhkan: pip install ultralytics opencv-python
  2. Masukkan gambar yang ingin diuji ke dalam folder projek
  3. Jalankan program dengan menekan ikon run code atau dengan: Python main.py
  4. Hasil deteksi akan muncul dalam jendela OpenCV.

# Penjelasakan Kode:
- `from ultralytics import YOLO` (Digunakan untuk memanggil model YOLOv11_
- 'import cv2' (Digunakan untuk menampilkan gambar hasil deteksi)
- 'model = YOLO('best.pt')' (Digunakan untuk memuat model hasil training yang telah dibuat sebelumnya di Google                                           Colab)
- 'path_gambar = 'gambar_test.jpg'' (Menentukan lokasi gambar yang akan dideteksi)
- 'results = model.predict(source=path_gambar, conf=0.5)' (Model melakukan proses prediksi pada gambar dengan confidence                                                                threshold sebesar 0.5)
