# Game Tembak-Tembakan dengan Pygame

Kode ini adalah implementasi sederhana dari permainan tembak-tembakan yang dibuat menggunakan library Pygame. Dalam permainan ini, pemain mengendalikan karakter (gambar pemain) dan harus menembak musuh (gambar musuh) yang datang dari atas layar. Berikut adalah penjelasan singkat tentang bagaimana kode ini berfungsi:

1. **Inisialisasi Pygame**: Kode dimulai dengan menginisialisasi Pygame.

2. **Warna**: Kode mendefinisikan warna putih (WHITE) yang akan digunakan dalam permainan.

3. **Ukuran Layar**: Layar permainan memiliki lebar dan tinggi yang ditentukan.

4. **Membuat Layar**: Pygame membuat layar dengan ukuran yang telah ditentukan dan memberikan judul "Game Tembak-Tembakan".

5. **Karakter Pemain**: Kode memuat gambar karakter pemain dan mengatur posisinya di bagian bawah layar. Kecepatan pemain juga diatur.

6. **Peluru**: Kode memuat gambar peluru, mengatur kecepatan peluru, dan menentukan status awal peluru ("ready" atau "fire").

7. **Musuh**: Musuh akan muncul dari atas layar secara acak. Kode mengatur kecepatan musuh dan waktu spawn musuh.

8. **Skor**: Kode mengatur variabel skor dan font untuk menampilkan skor di layar.

9. **Fungsi-fungsi**: Terdapat beberapa fungsi untuk menggambar pemain, peluru, musuh, dan mengecek tabrakan antara peluru dan musuh.

10. **Game Loop**: Kode berjalan dalam sebuah game loop utama. Loop ini mendeteksi input pemain, menggerakkan pemain, menggambar elemen-elemen permainan, mengecek tabrakan, mengupdate skor, dan mengupdate layar.

11. **Menutup Pygame**: Setelah pemain kalah atau keluar dari permainan, Pygame dihentikan.

## Menjalankan Kode

Anda dapat menjalankan kode ini jika Anda telah menginstal Pygame. Anda dapat menginstalnya dengan perintah berikut:

```bash
pip install pygame
```

1. Salin kode di atas dan simpan dalam sebuah file dengan ekstensi `.py`.

2. Pastikan Anda memiliki gambar karakter pemain ("player.png"), gambar musuh ("enemy.png"), dan gambar peluru ("bullet.png") dalam direktori yang sama dengan file Python Anda.

3. Jalankan file tersebut dengan perintah berikut melalui terminal:

   ```bash
   python nama_file.py
   ```

   Gantilah `nama_file.py` dengan nama file tempat Anda menyimpan kode ini.

## Hasil

Setelah kode dijalankan, jendela permainan "Game Tembak-Tembakan" akan muncul. Anda dapat mengendalikan karakter pemain dengan menggunakan tombol panah kiri dan kanan pada keyboard, dan menembak dengan tombol spasi. Skor Anda akan ditampilkan di sudut kiri atas layar. Tujuan permainan adalah menembak sebanyak mungkin musuh tanpa biarkan mereka mencapai pemain.

Selamat bermain!
