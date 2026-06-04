# Kelompok 6
1. Anis Syarifatul Mursyidah (G1A023036)
2. M. Aimar Apda Hadis (G1A023048)
3. Arrafi Andersont (G1A023090)

# Proyek Deteksi Kaganga
Proyek ini merupakan sistem deteksi objek untuk mengenali aksara Kaganga menggunakan model YOLOv11 dari library Ultralytics YOLO. Model dilatih menggunakan dataset dari Roboflow melalui Google Colab, kemudian hasil model digunakan untuk melakukan deteksi pada gambar secara lokal menggunakan Python.

# Dataset
Dataset yang digunakan pada proyek ini diperoleh dari platform Roboflow dan berisi citra aksara Kaganga yang telah melalui proses anotasi untuk kebutuhan object detection.

Dataset dibagi menjadi tiga bagian utama agar model dapat dilatih dan diuji dengan baik:
- Train Data (1437 Images): Digunakan untuk melatih model dalam mengenali pola dan bentuk aksara Kaganga.
- Validation Data (167 Images): Digunakan untuk mengevaluasi performa model selama proses training berlangsung.
- Test Data (65 Images): Digunakan untuk menguji kemampuan akhir model terhadap data yang belum pernah dilihat sebelumnya.

Dataset:
https://universe.roboflow.com/novalrizkiansyah-ymail-com/aksara-ulu-rejang

# Training Model
Proses training model dilakukan menggunakan Google Colab dengan memanfaatkan akselerasi GPU agar proses pelatihan berjalan lebih cepat dan efisien.

Model yang digunakan adalah YOLOv11 dari library Ultralytics. Training dilakukan selama 100 epoch menggunakan dataset yang terhubung melalui file data.yaml.

Konfigurasi training yang digunakan:

```
from ultralytics import YOLO

model = YOLO('yolov11n.pt')

model.train(
    data='data.yaml',
    epochs=100,
    imgsz=640
)
```

Penjelasan konfigurasi:

- `data.yaml` digunakan untuk menghubungkan dataset training.
- `epochs=100` digunakan agar model belajar lebih optimal.
- `imgsz=640` digunakan sebagai ukuran input gambar pada proses training.

Hasil training menghasilkan file model best.pt yang kemudian digunakan pada proses deteksi aksara Kaganga.

# Fitur
- Deteksi aksara Kaganga pada gambar
- Menggunakan model hasil training di Google Colab (best.pt)
- Menampilkan hasil deteksi secara langsung
- Menggunakan YOLOv11 untuk proses object detection

# Struktur Folder
- ├── best.pt ---> Model hasil training
- ├── gambar_test.jpg ---> Gambar untuk diuji
- ├── main.py ---> Program utama
- └── README.md

# Cara Menjalankan Program
  1. Pastikan Python sudah terpasang pada komputer
  2. Install library yang dibutuhkan `pip install ultralytics opencv-python`
  3. Masukkan gambar yang ingin diuji ke dalam folder proyek
  4. Jalankan program dengan menekan ikon run code atau dengan `Python main.py`
  5. Hasil deteksi akan muncul dalam jendela OpenCV

# Penjelasakan Kode
- `from ultralytics import YOLO` (Digunakan untuk memanggil model YOLOv11)
- `import cv2` (Digunakan untuk menampilkan gambar hasil deteksi)
- `model = YOLO('best.pt')` (Digunakan untuk memuat model hasil training yang telah dibuat sebelumnya di Google Colab)
- `path_gambar = 'gambar_test.jpg'` (Menentukan lokasi gambar yang akan dideteksi)
- `results = model.predict(source=path_gambar, conf=0.5)` (Model melakukan proses prediksi pada gambar dengan confidence threshold sebesar 0.5)
