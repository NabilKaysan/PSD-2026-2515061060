# Implementasi Sequential Search pada Sistem Pencarian Slot Parkir Kosong di Mall

## a. Judul Program
Sistem Pencarian Slot Parkir Kosong di Mall

## b. Deskripsi Singkat
Program ini merupakan implementasi algoritma Sequential Search dalam studi kasus pencarian slot parkir kosong di mall. Program dibuat menggunakan bahasa Python dan mensimulasikan kondisi parkir modern, di mana sistem akan memeriksa setiap slot parkir secara berurutan untuk menemukan slot yang berstatus "Kosong".

Struktur data yang digunakan adalah list, di mana setiap elemen menyimpan data slot parkir berupa kode slot, status slot, lantai parkir, dan jenis kendaraan. Sistem ini menerapkan konsep pencarian sekuensial, yaitu data dicek satu per satu dari awal hingga ditemukan slot yang sesuai atau sampai data habis diperiksa. Operasi utama dalam program ini adalah mencari slot kosong pertama dan menampilkan data slot parkir yang tersedia.

## c. Source Code

### 1. Fungsi Sequential Search

<img width="1492" height="1008" alt="tugas_akhir_judul3 py" src="https://github.com/user-attachments/assets/e9011fde-ef64-426f-a4e2-efa9b324a2d4" />

**Penjelasan:**
- `def sequential_search(slot_parkir, n, target):`  
  Mendefinisikan fungsi pencarian sekuensial dengan parameter data slot parkir, jumlah data, dan target status yang dicari.
- `i = 0`  
  Variabel indeks untuk memulai pencarian dari elemen pertama.
- `counter = 0`  
  Variabel penghitung jumlah data yang cocok dengan target.
- `posisi = []`  
  Menyimpan indeks slot yang sesuai dengan target.
- `while i < n:`  
  Melakukan perulangan selama indeks masih berada dalam batas data.
- `if slot_parkir[i][1].lower() == target.lower():`  
  Mengecek apakah status slot pada indeks ke-`i` sama dengan target.
- `counter += 1` dan `posisi.append(i)`  
  Jika cocok, jumlah data bertambah dan indeks disimpan.
- `i += 1`  
  Melanjutkan pencarian ke slot berikutnya.
- `return counter, posisi`  
  Mengembalikan jumlah data yang ditemukan beserta daftar indeksnya.

### 2. Fungsi Utama Program

<img width="1968" height="2682" alt="tugas_akhir_judul3 py (1)" src="https://github.com/user-attachments/assets/6726f5ec-ee8e-463f-9664-6ba45bf7ba71" />

**Penjelasan:**
- `slot_parkir` berisi daftar data parkir yang akan dicari.
- `n = len(slot_parkir)` menghitung jumlah data.
- Program menampilkan seluruh data slot parkir terlebih dahulu.
- Pengguna diminta memasukkan status yang ingin dicari, yaitu `Kosong` atau `Terisi`.
- Data kemudian diproses menggunakan fungsi `sequential_search()`.
- Jika data ditemukan, program menampilkan jumlah kemunculan dan detail slot parkir.
- Jika tidak ditemukan, program menampilkan pesan bahwa data tidak tersedia.

## d. Output Program

### Program akan menampilkan data slot parkir dan meminta input status yang dicari

Contoh tampilan awal program:

<img width="443" height="242" alt="Screenshot 2026-05-07 210414" src="https://github.com/user-attachments/assets/3c5e8bdf-4a8a-44f3-a384-e740f22b090b" />

### Contoh Output Saat User Menginputkan "Terisi"
<img width="506" height="597" alt="Screenshot 2026-05-07 210543" src="https://github.com/user-attachments/assets/f56a416c-66c5-442e-98df-3fb2c15e131d" />

### Contoh Output Saat User Menginputkan "Kosong"
<img width="518" height="466" alt="Screenshot 2026-05-07 210603" src="https://github.com/user-attachments/assets/88804833-360f-4d2c-8797-3223231c6b0b" />


### Penjelasan Output
- Saat program dijalankan, seluruh data slot parkir akan ditampilkan terlebih dahulu.
- Pengguna kemudian memasukkan status yang ingin dicari.
- Program akan mengecek setiap data slot parkir satu per satu.
- Jika status yang dicari adalah `Kosong`, maka program menampilkan seluruh slot yang masih tersedia.
- Jika status yang dicari adalah `Terisi`, maka program menampilkan seluruh slot yang telah diisi.
- Jika status tidak ditemukan, program menampilkan pesan bahwa data tidak tersedia.

### Kesimpulan Output
- Output program menunjukkan bahwa algoritma Sequential Search bekerja dengan memeriksa data secara berurutan.
- Pencarian dilakukan dari awal list hingga seluruh data selesai diperiksa.
- Sistem ini sesuai untuk studi kasus pencarian slot parkir kosong karena data dapat dicek satu per satu secara sederhana dan mudah dipahami.

## e. Link Youtube
https://youtu.be/lG0vK7xzVFo
