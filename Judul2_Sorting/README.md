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
### Screenshoot Output

<img width="707" height="715" alt="Screenshot 2026-05-04 204048" src="https://github.com/user-attachments/assets/06d6bf19-3bbb-453c-b6a1-21ad8a2fa944" />

### Penjelasan Output
- Ketika program dijalankan, pengguna diminta memasukkan jumlah masakan yang akan diproses.
- Setelah itu, pengguna memasukkan data setiap masakan yang terdiri dari nama masakan, waktu masak, tingkat kesulitan, dan target waktu siap.
- Pada bagian **Data sebelum diurutkan**, program menampilkan seluruh data yang masih berada dalam urutan input awal.
- Data masakan kemudian dihitung skor prioritasnya menggunakan fungsi `hitung_skor()`, yaitu dengan menjumlahkan waktu masak dan tingkat kesulitan.
- Dari hasil perhitungan, diperoleh skor masing-masing data, yaitu:
  - Gulai = 115
  - Nasi = 60
  - Mie = 40
  - Nugget = 15
- Setelah proses perhitungan skor selesai, program melakukan pengurutan menggunakan algoritma Insertion Sort dengan urutan dari skor terbesar ke skor terkecil.
- Hasil akhirnya menampilkan urutan memasak yang disarankan, yaitu Gulai, Nasi, Mie, dan Nugget.
- Data target waktu siap tetap tersimpan pada setiap data masakan, tetapi pada coding ini belum digunakan dalam proses penghitungan skor, sehingga hanya menjadi informasi tambahan.
### Kesimpulan Output
- Output program menunjukkan bahwa proses pengurutan berjalan sesuai dengan algoritma Insertion Sort.
- Masakan dengan skor prioritas paling tinggi akan ditempatkan di urutan teratas.
- Dengan demikian, program dapat membantu menentukan urutan memasak secara lebih teratur dan efisien.
## e. Link Youtube
https://youtu.be/1lNkfJRFkrk
