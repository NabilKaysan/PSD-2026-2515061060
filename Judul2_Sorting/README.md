# Implementasi Insertion Sort pada Smart Cooking Scheduler

## a. Judul Program
Sistem Penentuan Urutan Memasak pada Smart Cooking Scheduler

## b. Deskripsi Singkat
Program ini merupakan implementasi algoritma sorting menggunakan metode Insertion Sort pada studi kasus kehidupan sehari-hari, yaitu pengaturan urutan memasak beberapa menu agar proses memasak menjadi lebih teratur dan efisien.

Pada program ini, setiap masakan memiliki data berupa nama masakan, waktu masak, tingkat kesulitan, dan target waktu siap. Data tersebut kemudian diurutkan berdasarkan skor prioritas. Skor prioritas digunakan untuk menentukan masakan mana yang sebaiknya dikerjakan terlebih dahulu.

Struktur data yang digunakan adalah list Python, sedangkan algoritma sorting yang diterapkan adalah Insertion Sort. Algoritma ini bekerja dengan cara menyisipkan elemen pada posisi yang sesuai di dalam data yang sudah terurut sebagian.

## c. Source Code

<img width="1988" height="3168" alt="tugas_akhir_judul2 py (2)" src="https://github.com/user-attachments/assets/4d94b0e2-ef51-4f96-8b10-3567c1103097" />



### 1. Fungsi `hitung_skor()`

- `def hitung_skor(masakan):`
  - Mendefinisikan fungsi untuk menghitung skor prioritas.

- `return masakan[1] + masakan[2]`
  - Mengembalikan nilai waktu masak + tingkat kesulitan.
  - Semakin besar skor → semakin diprioritaskan.

---

### 2. Fungsi `insertion_sort()`

- `def insertion_sort(arr, n):`
  - Fungsi untuk mengurutkan data menggunakan insertion sort.

- `for i in range(1, n):`
  - Perulangan dimulai dari elemen ke-2.

- `temp = arr[i]`
  - Menyimpan data sementara.

- `j = i - 1`
  - Menentukan posisi sebelumnya.

- `while j >= 0 and hitung_skor(arr[j]) < hitung_skor(temp):`
  - Membandingkan skor dan menggeser data.

- `arr[j + 1] = arr[j]`
  - Menggeser elemen ke kanan.

- `j -= 1`
  - Pindah ke indeks sebelumnya.

- `arr[j + 1] = temp`
  - Menyisipkan elemen ke posisi yang benar.

---

### 3. Fungsi `main()`

- `def main():`
  - Fungsi utama program.

- `try:`
  - Menangani error input.

- `n = int(input("Masukkan jumlah masakan: "))`
  - Input jumlah data.

- `arr = []`
  - List kosong untuk data.

- `for i in range(n):`
  - Loop input data.

- `while True:`
  - Validasi input.

- `arr.append([nama, waktu, sulit, target])`
  - Menyimpan data.

- `insertion_sort(arr, n)`
  - Memanggil sorting.

- `print("\nUrutan memasak yang disarankan:")`
-   `for i in range(n):`
-    `print(f"{arr[i][0]} (Skor: {hitung_skor(arr[i])})")`
  - Menampilkan hasil.

---

### 4. Struktur Program

- `if __name__ == "__main__":`
  - Entry point program.

- `main()`
  - Menjalankan program.


## d. Output Program
Misalnya data yang dimasukkan sebagai berikut:

1. Nasi Goreng, 20 menit, kesulitan 40, target 60  
2. Sup Ayam, 35 menit, kesulitan 60, target 60  
3. Telur Dadar, 10 menit, kesulitan 20, target 60  
4. Sambal, 5 menit, kesulitan 30, target 60  

## e. Contoh Hasil Keluaran
Setelah data diurutkan, masakan dengan skor prioritas lebih tinggi akan berada di urutan awal, sehingga proses memasak menjadi lebih teratur.

hami karena prosesnya dilakukan dengan cara menyisipkan elemen ke posisi yang tepat secara bertahap.
