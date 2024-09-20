# Quiz Kriptografi

Muhammad Rifqy Nirwandi

4611422088

Kriptografi
## Overview Program
Program ini adalah alat untuk mengenkripsi dan mendekripsi teks menggunakan tiga jenis cipher:
- Vigenere Cipher

Cara Kerja: Menggunakan kunci untuk menggeser setiap huruf dalam teks. Misalnya, jika huruf dalam teks adalah A dan kuncinya B, maka A akan digeser menjadi B.
Input: Teks dan kunci. Kunci harus panjangnya minimal 12 karakter (kecuali untuk Hill Cipher).
Fungsi: `vigenere_cipher(text, key, encrypt)` untuk melakukan enkripsi atau dekripsi.
- Playfair Cipher

Cara Kerja: Menggunakan matriks 5x5 yang diisi dengan huruf dari kunci dan sisa huruf dari alfabet (tanpa huruf J). Teks dibagi menjadi pasangan huruf, dan setiap pasangan diproses berdasarkan posisi dalam matriks.
Input: Teks dan kunci. Huruf J akan diubah menjadi I.
Fungsi: `playfair_cipher(text, key, encrypt)` untuk enkripsi atau dekripsi.
- Hill Cipher

Cara Kerja: Menggunakan operasi matriks. Kunci harus berbentuk matriks 2x2. Setiap dua huruf dalam teks diproses menggunakan kunci.
Input: Teks dan kunci dalam bentuk matriks (misalnya, 6 24\n1 13).
Fungsi: `hill_cipher(text, key, encrypt)` untuk enkripsi atau dekripsi.

## Struktur Program
- Import Library: Program menggunakan `tkinter` untuk membuat antarmuka pengguna grafis (GUI).
- Fungsi Utama:
1. `encrypt_decrypt()`: Fungsi ini mengambil teks dan kunci dari input, kemudian memanggil fungsi cipher yang sesuai berdasarkan pilihan pengguna (Vigenere, Playfair, atau Hill) untuk mengenkripsi atau mendekripsi teks.
2. `upload_file()`: Memungkinkan pengguna untuk mengunggah file teks yang berisi pesan untuk diproses.
- Antarmuka Pengguna (UI):
1. Beberapa label dan input untuk teks, kunci, dan pilihan cipher.
2. Tombol untuk mengunggah file dan memproses teks.
3. Area untuk menampilkan hasil.

## Penggunaan Program
1. Input Teks: Masukkan teks yang ingin dienkripsi atau didekripsi di kotak teks.
2. Input Kunci: Masukkan kunci yang akan digunakan (panjang minimal 12 karakter untuk Vigenere dan Playfair, dan bentuk matriks 2x2 untuk Hill).
3. Pilih Jenis Cipher: Pilih jenis cipher yang ingin digunakan.
4. Operasi: Pilih apakah ingin mengenkripsi atau mendekripsi.
5. Proses: Klik tombol "Proses" untuk mendapatkan hasilnya. Hasil akan ditampilkan di area hasil di bawah.