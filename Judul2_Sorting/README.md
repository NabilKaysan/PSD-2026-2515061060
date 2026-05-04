# Implementasi Insertion Sort pada Smart Cooking Scheduler

## a. Judul Program
Sistem Penentuan Urutan Memasak pada Smart Cooking Scheduler

## b. Deskripsi Singkat
Program ini merupakan implementasi algoritma sorting menggunakan metode Insertion Sort pada studi kasus kehidupan sehari-hari, yaitu pengaturan urutan memasak beberapa menu agar proses memasak menjadi lebih teratur dan efisien.

Pada program ini, setiap masakan memiliki data berupa nama masakan, waktu masak, tingkat kesulitan, dan target waktu siap. Data tersebut kemudian diurutkan berdasarkan skor prioritas. Skor prioritas digunakan untuk menentukan masakan mana yang sebaiknya dikerjakan terlebih dahulu.

Struktur data yang digunakan adalah list Python, sedangkan algoritma sorting yang diterapkan adalah Insertion Sort. Algoritma ini bekerja dengan cara menyisipkan elemen pada posisi yang sesuai di dalam data yang sudah terurut sebagian.

## c. Source Code

<img width="1988" height="3502" alt="tugas_akhir_judul2 py (1)" src="https://github.com/user-attachments/assets/6cbf0b4e-8a7b-49ff-b2ee-5e2a058fb42c" />


### 1. Fungsi `hitung_skor()`
- `def hitung_skor(masakan):`
  - Fungsi ini digunakan untuk menghitung skor prioritas dari setiap masakan.
- `nama = masakan[0]`
  - Menyimpan nama masakan.
- `waktu = masakan[1]`
  - Menyimpan waktu masak.
- `sulit = masakan[2]`
  - Menyimpan tingkat kesulitan.
- `target = masakan[3]`
  - Menyimpan target waktu siap masakan.
- `return waktu + sulit`
  - Menghasilkan skor prioritas berdasarkan waktu masak dan tingkat kesulitan.
  - Pada versi ini, target disimpan sebagai data tambahan untuk pengembangan berikutnya.

### 2. Fungsi `insertion_sort()`
- `def insertion_sort(arr, n):`
  - Fungsi untuk mengurutkan data masakan menggunakan algoritma Insertion Sort.
- `for i in range(1, n):`
  - Perulangan dimulai dari elemen ke-2 karena elemen pertama dianggap sudah terurut.
- `temp = arr[i]`
  - Menyimpan elemen yang sedang diproses.
- `j = i - 1`
  - Menentukan posisi elemen sebelumnya.
- `while j >= 0 and hitung_skor(arr[j]) < hitung_skor(temp):`
  - Jika skor elemen sebelumnya lebih kecil dari skor elemen saat ini, elemen tersebut digeser ke kanan.
- `arr[j + 1] = temp`
  - Menempatkan elemen pada posisi yang sesuai.

### 3. Fungsi `main()`
- `def main():`
  - Fungsi utama program.
- `try:`
  - Digunakan untuk menangkap error jika input jumlah data bukan angka.
- `n = int(input("Masukkan jumlah masakan: "))`
  - Memasukkan jumlah data masakan yang akan diurutkan.
- `arr = []`
  - Menampung data masakan dalam list.
- `for i in range(n):`
  - Perulangan untuk menginput data masakan satu per satu.
- `nama = input("Nama masakan: ")`
  - Menginput nama masakan.
- `waktu = int(input("Waktu masak (menit): "))`
  - Menginput waktu masak.
- `sulit = int(input("Tingkat kesulitan (1-100): "))`
  - Menginput tingkat kesulitan masakan.
- `target = int(input("Target waktu siap: "))`
  - Menginput target waktu selesai masakan.
- `arr.append([nama, waktu, sulit, target])`
  - Menyimpan data masakan ke dalam list.
- `print("\nData sebelum diurutkan:")`
  - Menampilkan data sebelum sorting.
- `insertion_sort(arr, n)`
  - Memanggil fungsi sorting.
- `print("\nUrutan memasak yang disarankan:")`
  - Menampilkan hasil pengurutan data setelah sorting.

## d. Contoh Data Masukan
Misalnya data yang dimasukkan sebagai berikut:

1. Nasi Goreng, 20 menit, kesulitan 40, target 60  
2. Sup Ayam, 35 menit, kesulitan 60, target 60  
3. Telur Dadar, 10 menit, kesulitan 20, target 60  
4. Sambal, 5 menit, kesulitan 30, target 60  

## e. Contoh Hasil Keluaran
Setelah data diurutkan, masakan dengan skor prioritas lebih tinggi akan berada di urutan awal, sehingga proses memasak menjadi lebih teratur.

## f. Kesimpulan
Program ini menunjukkan penerapan algoritma Insertion Sort dalam kehidupan sehari-hari, yaitu pada sistem penentuan urutan memasak. Dengan pendekatan ini, pengguna dapat menentukan masakan mana yang perlu dikerjakan lebih dulu berdasarkan prioritas yang telah dihitung.

Algoritma Insertion Sort cocok digunakan untuk data yang jumlahnya tidak terlalu banyak dan mudah dipahami karena prosesnya dilakukan dengan cara menyisipkan elemen ke posisi yang tepat secara bertahap.
