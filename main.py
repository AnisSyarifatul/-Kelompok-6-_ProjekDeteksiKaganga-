from ultralytics import YOLO
import cv2
import os

# Model YOLO hasil training dari google collab
model = YOLO('best.pt')

path_gambar = 'gambar_test.jpg'

if os.path.exists(path_gambar):
    results = model.predict(source=path_gambar, conf=0.5)
    
    res_plotted = results[0].plot()
    
    cv2.imshow("Hasil Deteksi Aksara Kaganga", res_plotted)
    
    print("Jendela terbuka. Tekan tombol apa saja pada keyboard untuk menutup.")
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
else:
    print(f"Error: File {path_gambar} tidak ditemukan di folder proyek!")