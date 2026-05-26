# Implementasi Binary Search Tree pada Smart Fridge

## a. Judul Program

**Sistem Monitoring Makanan Berdasarkan Tanggal Kedaluwarsa Menggunakan Binary Search Tree (BST)**

## b. Deskripsi Singkat

Program ini merupakan implementasi struktur data **Binary Search Tree (BST)** dengan studi kasus **Smart Fridge** atau kulkas pintar. Program dibuat menggunakan bahasa Python untuk membantu mengelola data makanan berdasarkan tanggal kedaluwarsa.

Setiap makanan disimpan pada node BST dengan tanggal kedaluwarsa sebagai key utama. Data dengan tanggal kedaluwarsa yang lebih kecil akan ditempatkan pada subtree kiri, sedangkan data dengan tanggal yang lebih besar akan ditempatkan pada subtree kanan. Dengan demikian, data makanan dapat tersusun secara otomatis dan terurut berdasarkan waktu kedaluwarsa.

Operasi utama dalam program ini meliputi penambahan data makanan (*insert*), pencarian data makanan (*search*), menampilkan seluruh data secara terurut (*inorder*), mencari makanan yang paling cepat kedaluwarsa (*find_min*), mencari makanan yang paling lama kedaluwarsa (*find_max*), menghitung jumlah makanan (*count_nodes*), dan menghitung tinggi pohon (*height*).

## c. Source Code

### 1. Class Node

<img width="1124" height="684" alt="tugas_akhir_judul5 py" src="https://github.com/user-attachments/assets/df66c0d7-e8dc-479c-9935-f419c656b37e" />


- `class Node:`  
  Mendefinisikan class Node sebagai elemen dasar pada BST.

- `def __init__(self, expired, nama):`  
  Constructor untuk menginisialisasi data node.

- `self.expired = expired`  
  Menyimpan tanggal kedaluwarsa sebagai key.

- `self.nama = nama`  
  Menyimpan nama makanan.

- `self.left = None`  
  Pointer ke anak kiri.

- `self.right = None`  
  Pointer ke anak kanan.

### 2. Class SmartFridge

<img width="1000" height="522" alt="tugas_akhir_judul5 py (1)" src="https://github.com/user-attachments/assets/38805b16-fae0-45b0-9e62-140126c1aef6" />


- `class SmartFridge:`  
  Mendefinisikan class utama untuk mengelola BST.

- `def __init__(self):`  
  Constructor untuk inisialisasi BST.

- `self.root = None`  
  Menandakan bahwa BST masih kosong.

### 3. Fungsi insert_node()

<img width="1692" height="1008" alt="tugas_akhir_judul5 py (2)" src="https://github.com/user-attachments/assets/45b27c62-b921-4430-a5f4-d48bb16f0c57" />


- Fungsi ini digunakan untuk menambahkan node baru ke BST.
- Jika root kosong, maka node baru langsung dibuat.
- Jika tanggal kedaluwarsa lebih kecil dari root, maka data dimasukkan ke subtree kiri.
- Jika tanggal kedaluwarsa lebih besar dari root, maka data dimasukkan ke subtree kanan.
- Fungsi dilakukan secara rekursif sampai posisi yang sesuai ditemukan.

### 4. Fungsi insert()

<img width="1644" height="468" alt="tugas_akhir_judul5 py (3)" src="https://github.com/user-attachments/assets/947f467e-40bb-4b3c-8c3a-868b15e7bdf2" />


- Fungsi ini berfungsi sebagai pembungkus dari `insert_node()`.
- Digunakan untuk memulai proses penambahan data dari root.

### 5. Fungsi search_node()

<img width="1492" height="954" alt="tugas_akhir_judul5 py (4)" src="https://github.com/user-attachments/assets/f27dcb7d-6aaa-4a5c-aecb-b82aea0275b9" />


- Fungsi ini digunakan untuk mencari data makanan berdasarkan tanggal kedaluwarsa.
- Jika node kosong, maka data tidak ditemukan.
- Jika nilai yang dicari sama dengan key node, maka data ditemukan.
- Jika lebih kecil, pencarian dilakukan ke kiri.
- Jika lebih besar, pencarian dilakukan ke kanan.

### 6. Fungsi search()

<img width="1406" height="468" alt="tugas_akhir_judul5 py (5)" src="https://github.com/user-attachments/assets/a0d8c9c3-ce4a-4120-aa09-e2f1e4f682a8" />


- Fungsi ini digunakan untuk memulai pencarian dari root BST.

### 7. Fungsi inorder()

<img width="1298" height="684" alt="tugas_akhir_judul5 py (6)" src="https://github.com/user-attachments/assets/7d435981-0e14-4bbb-8df0-ccf4ebad4d8a" />


- Fungsi ini menggunakan traversal inorder.
- Urutan traversal:
  1. Kunjungi subtree kiri.
  2. Tampilkan node saat ini.
  3. Kunjungi subtree kanan.
- Karena BST menyimpan nilai yang lebih kecil di kiri dan lebih besar di kanan, hasil inorder akan tampil terurut secara otomatis.

### 8. Fungsi find_min()

<img width="1146" height="792" alt="tugas_akhir_judul5 py (7)" src="https://github.com/user-attachments/assets/88d29807-3b52-47c8-abde-5303912d057c" />


- Fungsi ini digunakan untuk mencari node dengan nilai terkecil.
- Pada BST, nilai terkecil selalu berada pada node paling kiri.
- Dalam studi kasus Smart Fridge, fungsi ini digunakan untuk mengetahui makanan yang paling cepat kedaluwarsa.

### 9. Fungsi find_max()

<img width="1168" height="738" alt="tugas_akhir_judul5 py (8)" src="https://github.com/user-attachments/assets/9dad175a-5e3e-412d-9081-35fe9f24000a" />


- Fungsi ini digunakan untuk mencari node dengan nilai terbesar.
- Pada BST, nilai terbesar selalu berada pada node paling kanan.
- Dalam program ini, fungsi digunakan untuk mengetahui makanan yang paling lama kedaluwarsa.

### 10. Fungsi count_nodes()

<img width="1692" height="630" alt="tugas_akhir_judul5 py (9)" src="https://github.com/user-attachments/assets/dab52596-f95c-440f-bab1-b13f04e736a1" />


- Fungsi ini digunakan untuk menghitung jumlah seluruh node pada BST.
- Perhitungan dilakukan dengan menjumlahkan node saat ini, subtree kiri, dan subtree kanan.

### 11. Fungsi height()

<img width="1362" height="738" alt="tugas_akhir_judul5 py (10)" src="https://github.com/user-attachments/assets/9213cd56-151a-458b-8d7e-6361a76e12e5" />


- Fungsi ini digunakan untuk menghitung tinggi pohon BST.
- Tinggi pohon menunjukkan kedalaman maksimum struktur BST.

### 12. Fungsi main()

<img width="1692" height="4680" alt="tugas_akhir_judul5 py (11)" src="https://github.com/user-attachments/assets/85ef5c27-b2cb-4bb1-8df2-7bca8ab58a1d" />


- Fungsi utama program yang digunakan untuk:
  - Menampilkan menu.
  - Menerima input pengguna.
  - Menjalankan operasi BST sesuai pilihan menu.
  - Mengakhiri program ketika pengguna memilih keluar.

### 13. Penjelasan Menu Program

#### Menu 1 : Tambah Makanan
Digunakan untuk memasukkan data makanan baru ke dalam BST berdasarkan tanggal kedaluwarsa.

#### Menu 2 : Cari Makanan
Digunakan untuk mencari data makanan berdasarkan tanggal kedaluwarsa tertentu.

#### Menu 3 : Tampilkan Makanan
Digunakan untuk menampilkan seluruh data makanan secara terurut menggunakan inorder traversal.

#### Menu 4 : Makanan Terdekat Kedaluwarsa
Digunakan untuk menampilkan makanan dengan tanggal kedaluwarsa paling kecil.

#### Menu 5 : Makanan Paling Awet
Digunakan untuk menampilkan makanan dengan tanggal kedaluwarsa paling besar.

#### Menu 6 : Jumlah Makanan
Digunakan untuk menghitung jumlah data makanan yang tersimpan.

#### Menu 7 : Tinggi Pohon
Digunakan untuk menghitung tinggi BST.

#### Menu 8 : Keluar
Digunakan untuk mengakhiri program.

## d. Penjelasan Output

Program akan menampilkan menu utama saat dijalankan  
Saat program pertama kali dijalankan, pengguna akan melihat menu utama untuk mengelola data makanan pada Smart Fridge.

<img width="329" height="256" alt="Screenshot 2026-05-26 193534" src="https://github.com/user-attachments/assets/7fb71d0f-7a0e-41c0-ae6f-c00843dd0b12" />


### Penjelasan Output

<img width="366" height="304" alt="Screenshot 2026-05-26 193617" src="https://github.com/user-attachments/assets/2d80bd1d-387f-4cf5-8776-19c00914f137" />

Ketika pengguna memilih menu 1, program akan meminta input:

- Tanggal expired
- Nama makanan

Data yang dimasukkan akan ditempatkan sesuai posisi pada Binary Search Tree berdasarkan tanggal kedaluwarsa.

<img width="317" height="291" alt="Screenshot 2026-05-26 193652" src="https://github.com/user-attachments/assets/1cd222d9-04dc-41a7-bf03-baa3c2bf3918" />

Ketika pengguna memilih menu 2, program akan mencari data makanan berdasarkan tanggal expired yang dimasukkan. Jika data ditemukan, program akan menampilkan nama makanan tersebut.

<img width="329" height="358" alt="Screenshot 2026-05-26 193754" src="https://github.com/user-attachments/assets/fda06cb9-86b3-426c-85ad-841791066ffb" />

Ketika pengguna memilih menu 3, program akan menampilkan seluruh data makanan secara terurut menggunakan inorder traversal.

<img width="457" height="274" alt="Screenshot 2026-05-26 193815" src="https://github.com/user-attachments/assets/1af11669-0022-4fb8-bae1-eeb67f2c22a3" />

Ketika pengguna memilih menu 4, program akan menampilkan makanan yang memiliki tanggal expired paling kecil atau paling cepat kedaluwarsa.

<img width="376" height="282" alt="Screenshot 2026-05-26 193826" src="https://github.com/user-attachments/assets/a73e52c5-3a00-4a29-98e0-d898c9c23b3a" />

Ketika pengguna memilih menu 5, program akan menampilkan makanan yang memiliki tanggal expired paling besar atau paling lama kedaluwarsa.

<img width="321" height="279" alt="Screenshot 2026-05-26 193836" src="https://github.com/user-attachments/assets/46844161-ceb4-402a-8b42-615c90a306dc" />

Ketika pengguna memilih menu 6, program akan menampilkan jumlah seluruh makanan yang tersimpan di dalam BST.

<img width="339" height="285" alt="Screenshot 2026-05-26 193845" src="https://github.com/user-attachments/assets/39dddc57-1f0b-4561-81a7-73c13f92d1ed" />
 
Ketika pengguna memilih menu 7, program akan menampilkan tinggi pohon BST.

<img width="318" height="258" alt="Screenshot 2026-05-26 193904" src="https://github.com/user-attachments/assets/4da5b5b5-4b8b-433e-a308-82a42912b2e7" />
  
Ketika pengguna memilih menu 8, program akan berhenti dan menampilkan pesan program selesai.

### Kesimpulan Output

Output program menunjukkan bahwa sistem pengelolaan makanan pada Smart Fridge berjalan sesuai konsep Binary Search Tree (BST), di mana:

- data makanan dimasukkan berdasarkan urutan tanggal kedaluwarsa,
- data dapat dicari dengan cepat menggunakan key tertentu,
- data dapat ditampilkan secara terurut melalui inorder traversal,
- makanan yang paling cepat dan paling lama kedaluwarsa dapat diketahui dengan mudah,
- serta jumlah data dan tinggi pohon BST dapat dihitung.

## e. Link YouTube
https://youtu.be/piU85z4FKew
