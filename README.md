# Kalibrasi Kamera
# Struktur Direktori
- calibration-camera-ver2.py adalah pyhton code untuk kalibrasi dan remove distorsi kamera
- create-chessboard.py adalah python code untuk membuat chessboard berdasarkan baris dan kolom yang kita mau
- getImages.py adalah python code untuk menangkap gambar dari kamera
- chessboard-custom.png adalah gambar chessboard berukuran 7x10
- /8-5 berisi gambar yang berhasil di kalibrasi
- /img merupakan folder untuk menaruh hasil tangkapan gambar dari getImages.py
- /dump merupakan temporary folder (dapat digunakan ketika ingin memindahkan melihat gambar mana saja yang bisa dikalibrasi setelah ditangkap pada folder /img dan sisa gambar yang tidak ingin dilihat ditaruh pada folder /dump)

# Permasalahan
Lihat folder /8-5 dan lihat gambar dengan posisi mana saja yang kurang<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20104620.png?raw=true)

# Langkah Perbaikan
1. Jalankan getImages.py dan buka chessboard-custom.png<br>
2. Arahkan kamera ke layar chessboard<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20103050.png?raw=true)
3. Tekan s (tidak menggunakan capslock)<br>
4. Gambar yang ditangkap akan masuk folder /img<br>
5. Setelah selesai melakukan penangkapan gambar, buka file calibration-camera-ver2.py<br>
6. Ubah path '8-5' menjadi 'img'<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20103227.png?raw=true)
7. Pastikan fungsi yang berjalan adalah runCalibration()<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20103332.png?raw=true)
8. Jalankan program<br>
9. Jika terdapat error seperti ini, artinya gambar tidak bisa di identifikasi dan harus dilakukan pengambilan gambar ulang<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20105621.png?raw=true)
10. Jika tidak terdapat error maka ubah nama file image menjadi posisi image ditangkap dan pindahkan ke folder /8-5<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20103446.png?raw=true)
11. Jika ingin menjalankan seluruh gambar pada folder /8-5 maka ubah kembali path 'img' menjadi '8-5'<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20103227.png?raw=true)
12. Jika sudah semua dikalibrasi, maka saatnya melakukan remove distorsi dengan mengubah path fungsi removeDistortion sesuai nama image yang kita mau<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20111804.png?raw=true)
14. Lalu pastikan mengaktifkan fungsi runRemoveDistortion()<br>
![Gambar](https://github.com/fransiskusabelpp/cam-calibration/blob/main/READMEimages/Screenshot%202024-03-13%20110228.png?raw=true)
