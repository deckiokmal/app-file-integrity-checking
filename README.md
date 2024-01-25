# Pemeriksaan Integritas File dengan Hashing (Python)
### Deskripsi:

Script Python ini diciptakan untuk memverifikasi integritas file dengan membandingkan nilai hash yang dihasilkan dengan nilai hash yang sudah diketahui. Script ini menggunakan algoritma hash SHA-1 dan SHA-256 untuk menghasilkan nilai hash yang aman dan andal.

## Fitur:
- Menerima `input file` dan `nilai hash` yang diharapkan.
- Menghitung nilai hash `SHA-1` dan `SHA-256` dari file yang diberikan.
- Membandingkan nilai hash yang dihitung dengan nilai hash yang diharapkan.
- Menampilkan pesan yang menginformasikan apakah file tersebut asli dan aman, atau telah dimodifikasi.

## Penggunaan:
- Simpan script ini dengan nama hash_generator.py.
- Buka terminal atau command prompt.
- Navigasikan ke direktori tempat script disimpan.
- Jalankan script dengan perintah berikut:
```
python hash_generator.py
```
- Masukkan nama file yang ingin diperiksa integritasnya (contoh: file.txt).
- Masukkan nilai hash yang diketahui untuk file tersebut (SHA-1 atau SHA-256).
- Script akan menampilkan hasil pemeriksaan integritas file.
```
Contoh Output:
Masukkan hash: 1f3870be274f6c49b3e31a0c6728957f3585e08e
Input filename (ex: file.txt): file.txt
hash sha1 match, your file is secure. 1f3870be274f6c49b3e31a0c6728957f3585e08e
```

## Referensi Python: `Working with File`
- [working with file](https://docs.python.org/3/library/pathlib.html)

## Persyaratan:

1. Python 3.x
2. Modul `hashlib` (biasanya sudah terpasang secara bawaan)

# Author:
[Decki Okmal Pratama]
