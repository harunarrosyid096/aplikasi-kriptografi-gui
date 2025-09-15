Aplikasi Kriptografi GUI (Tkinter)

Proyek ini adalah aplikasi GUI sederhana untuk melakukan **enkripsi dan dekripsi teks** menggunakan tiga algoritma kriptografi:

- Vigenère Cipher
- Affine Cipher
- AES (Advanced Encryption Standard, mode ECB

Dibuat menggunakan Python dan Tkinter.


  Fitur
- Enkripsi & dekripsi teks.
- Pilihan algoritma: Vigenère, Affine, AES.
- Tampilan sederhana berbasis Tkinter.
- Hasil langsung ditampilkan di aplikasi.

Instalasi & Menjalankan

1. Clone repository:
   ```bash
   git clone https://github.com/username/gui-kriptografi.git
   cd gui-kriptografi
2. Install dependensi:
   pip install pycryptodome
3.Jalankan aplikasi:
  python main.py

Penggunaan

Masukkan teks di kolom input.

Masukkan kunci:

Vigenère: masukkan string kunci (misalnya KEY).

Affine: masukkan dalam format a,b (contoh 5,8).

AES: masukkan string kunci (maks 16 karakter, jika kurang akan diisi 0).

Pilih algoritma (Vigenère, Affine, AES).

Pilih mode (Enkripsi atau Dekripsi).

Klik tombol Proses → hasil muncul di kolom output.
