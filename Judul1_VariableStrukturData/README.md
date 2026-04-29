# Implementasi Linked List pada Antrian Pelayanan SIM
## a. Judul Program
Sistem Antrian Pelayanan Pembuatan SIM
## b. Deskripsi Singkat
Program ini merupakan implementasi struktur data linked list dalam studi kasus antrian pelayanan pembuatan SIM. Program dibuat menggunakan bahasa Python dan mensimulasikan sistem antrian seperti di dunia nyata, di mana pemohon SIM akan dilayani berdasarkan urutan kedatangan.

Struktur data yang digunakan adalah singly linked list, di mana setiap elemen (node) memiliki data dan referensi ke node berikutnya. Sistem ini menerapkan konsep FIFO (First In First Out), yaitu data yang masuk terlebih dahulu akan diproses terlebih dahulu. Operasi utama dalam program ini meliputi penambahan antrian (enqueue), penghapusan antrian (dequeue), melihat antrian terdepan (peek), menampilkan seluruh antrian (display), dan menghitung jumlah antrian.
## c. Source Code
<img width="2032" height="7542" alt="2515061060_Muhammad Nabil Al Kaysan_Praktikum SD_TA 1 py" src="https://github.com/user-attachments/assets/cb7e616c-ced2-4d5c-b8ef-c022c528780b" />

### 1. Class Node
* `class Node:`
  * Mendefinisikan class Node sebagai elemen dasar dalam linked list.
* `def __init__(self, nomor, nama, jenis_sim):`
  * Constructor untuk menginisialisasi data pada node.
* `self.nomor = nomor`
  * Menyimpan nomor antrian.
* `self.nama = nama`
  * Menyimpan nama pemohon.
* `self.jenis_sim = jenis_sim`
  * Menyimpan jenis SIM yang diajukan.
* `self.next = None`
  * Pointer ke node berikutnya, awalnya bernilai None.
### 2. Class AntrianSIM
* `class AntrianSIM:`
  * Mendefinisikan class untuk mengelola sistem antrian.
* `def __init__(self):`
  * Constructor untuk inisialisasi antrian.
* `self.head = None`
  * Menunjuk node pertama (antrian depan).
* `self.tail = None`
  * Menunjuk node terakhir (antrian belakang).
* `self.total = 0`
  * Menyimpan jumlah total nomor antrian yang pernah dibuat.
### 3. Fungsi is_empty()
* `def is_empty(self):`
  * Fungsi untuk mengecek apakah antrian kosong.
* `return self.head is None`
  * Mengembalikan nilai True jika antrian kosong.
### 4. Fungsi enqueue()
* `def enqueue(self, nama, jenis_sim):`
  * Fungsi untuk menambahkan data ke antrian.
* `self.total += 1`
  * Menambahkan nomor antrian.
* `node_baru = Node(self.total, nama, jenis_sim)`
  * Membuat node baru dengan data pemohon.
* `if self.is_empty():`
  * Mengecek apakah antrian kosong.
* `self.head = node_baru`
* `self.tail = node_baru`
  * Jika kosong, node baru menjadi head dan tail.
* `else:`
* `self.tail.next = node_baru`
  * Jika tidak kosong, Menghubungkan node terakhir dengan node baru.
* `self.tail = node_baru`
  * Memindahkan tail ke node baru.
* `print(f"Antrian berhasil ditambahkan. Nomor antrian: {node_baru.nomor}")`
  * Menampilkan pesan bahwa data berhasil ditambahkan.
### 5. Fungsi dequeue()
* `def dequeue(self):`
  * Fungsi untuk menghapus data dari depan antrian.
* `if self.is_empty():`
  * Mengecek apakah antrian kosong.
* `print("Antrian kosong. Tidak ada peserta yang bisa dilayani.")`
* `return`
  * Jika kosong, tampilkan pesan dan keluar dari fungsi.
* `data_keluar = self.head`
  * Menyimpan node yang akan dihapus.
* `self.head = self.head.next`
  * Memindahkan head ke node berikutnya.
* `if self.head is None:`
  * Jika setelah penghapusan antrian kosong.
* `self.tail = None`
  * Set tail menjadi None.
* `print("\n=== PELAYANAN SIM ===")`
  * Menampilkan judul output pelayanan.
* `print(f"Nomor Antrian : {data_keluar.nomor}")`
* `print(f"Nama          : {data_keluar.nama}")`
* `print(f"Jenis SIM     : {data_keluar.jenis_sim}")`
  * Menampilkan data pemohon yang dilayani.
* `print("Status        : Telah dilayani")`
  * Menampilkan status pelayanan.
### 6. Fungsi peek()
* `def peek(self):`
  * Fungsi untuk melihat data terdepan tanpa menghapus.
* `if self.is_empty():`
    * `print("Antrian masih kosong.")`
  * Jika kosong, tampilkan pesan.
* `else:`
 * `print("\nAntrian terdepan:")`
  * Jika tidak kosong, Menampilkan judul.
* `print(f"Nomor Antrian : {self.head.nomor}")`
* `print(f"Nama          : {self.head.nama}")`
* `print(f"Jenis SIM     : {self.head.jenis_sim}")`
  * Menampilkan data node paling depan.
### 7. Fungsi display()
* `def display(self):`
  * Fungsi untuk menampilkan seluruh antrian.
* `if self.is_empty():`
    * `print("Antrian kosong.")`
    * `return`
* Jika kosong, tampilkan pesan.
* `print("\n=== DAFTAR ANTRIAN PELAYANAN SIM ===")`
  * Menampilkan judul daftar antrian.
* `current = self.head`
  * Menentukan node awal.
* `while current is not None:`
  * Melakukan traversal selama node masih ada.
* `print(f"[{current.nomor}] {current.nama} - SIM {current.jenis_sim}")`
  * Menampilkan data node saat ini.
* `current = current.next`
  * Berpindah ke node berikutnya.
### 8. Fungsi jumlah_antrian()
* `def jumlah_antrian(self):`
  * Fungsi untuk menghitung jumlah antrian.
* `count = 0`
  * Inisialisasi penghitung.
* `current = self.head`
  * Mulai dari node pertama.
* `while current is not None:`
  * `count += 1 `
  * `current = current.next`
  * Menelusuri seluruh node dan menghitung jumlahnya.
* `print(f"Jumlah antrian saat ini: {count}")`
  * Menampilkan jumlah antrian.
### 9. Fungsi menu()
* `def menu():`
  * Fungsi untuk menampilkan menu.
* `print("\n===== MENU ANTRIAN PELAYANAN SIM =====")`
* `print("1. Tambah antrian")`
* `print("2. Layani antrian")`
* `print("3. Lihat antrian terdepan")` 
* `print("4. Tampilkan seluruh antrian") `
* `print("5. Jumlah antrian")`
* `print("6. Keluar")`
  * Menampilkan daftar pilihan menu.
### 10. Fungsi main()
* `def main():`
  * Fungsi utama program.
* `antrian = AntrianSIM()`
  * Membuat objek antrian.
* `while True:`
  * `Perulangan program.`
  * `menu()`
  * Menampilkan menu.
* `try:`
  * `pilihan = int(input("Pilih menu: "))`
  * Mengambil input dari user.
* `except ValueError:`
   * `print("Input harus berupa angka.")`
   * `continue`
  * Menangani error jika input bukan angka.
### 11. Percabangan Menu
  ### Tambah Antrian
* `if pilihan == 1:`
  * Jika memilih tambah antrian.
* `nama = input("Masukkan nama pemohon: ").strip()`
* `jenis_sim = input("Masukkan jenis SIM (A/C/D): ").strip().upper()`
  * Mengambil input data.
* `if nama == "":`
* `print("Nama tidak boleh kosong.")`
* `continue`
  * Validasi nama.
* `if jenis_sim not in ["A", "C", "D"]:`
  * `print("Jenis SIM harus A, C, atau D.")`
  * `continue`
  * Validasi jenis SIM.
* `antrian.enqueue(nama, jenis_sim)`
  * Menambahkan data ke antrian.
  ### Layani Antrian
* `elif pilihan == 2:`
* `antrian.dequeue()`
  * Menghapus antrian terdepan.
  ### Lihat Antrian
* `elif pilihan == 3:`
* `antrian.peek()`
  * Menampilkan antrian terdepan.
  ### Tampilkan Semua
* `elif pilihan == 4:`
* `antrian.display()`
  * Menampilkan seluruh antrian.
  ### Jumlah Antrian
* `elif pilihan == 5:`
* `antrian.jumlah_antrian()`
  * Menampilkan jumlah antrian.
  ### Keluar
* `elif pilihan == 6:`
  * `print("Program selesai.")`
  * `break`
  *Menghentikan program.
  * `else:`
    * `print("Pilihan tidak valid.")`
### 12. Eksekusi Program
  * `if __name__ == "__main__":`
    * `main()`
  *Menjalankan fungsi utama saat file dieksekusi.

## d. Output Program
### Program akan menampilkan menu utama saat dijalankan

<img width="384" height="254" alt="Screenshot 2026-04-29 220559" src="https://github.com/user-attachments/assets/cee6244e-9fb5-497f-8bd4-b4b1c0b3f0c7" />

### Screenshoot Output

<img width="566" height="743" alt="Screenshot 2026-04-29 221358" src="https://github.com/user-attachments/assets/8ab3068d-743c-4e8e-a4e7-5f5a1cc18c61" />
<img width="544" height="717" alt="Screenshot 2026-04-29 221414" src="https://github.com/user-attachments/assets/b16077da-b015-46c9-a191-1b72cf5da28e" />
<img width="521" height="646" alt="Screenshot 2026-04-29 221423" src="https://github.com/user-attachments/assets/7df088f4-396b-46c0-a9f5-1d9db66a5460" />
<img width="543" height="762" alt="Screenshot 2026-04-29 221432" src="https://github.com/user-attachments/assets/76b81137-e7ff-4792-8fe4-84a444e01455" />

### Penjelasan Output
* Ketika pengguna memilih menu 1, program akan meminta input:
  * Nama pemohon
  * Jenis SIM (A/C/D)
Setiap penambahan data akan menambah nomor antrian secara otomatis (2, 3, dan seterusnya).
Data yang dimasukkan akan ditempatkan di bagian belakang antrian.
* Output Layani Antrian (Dequeue)
Ketika pengguna memilih menu 2, program akan memproses antrian paling depan.
* Output Lihat Antrian Terdepan (Peek)
Ketika memilih menu 3, program akan menampilkan data pemohon yang berada di posisi paling depan tanpa menghapusnya.
* Output Tampilkan Seluruh Antrian (Display)
Ketika memilih menu 4, program akan menampilkan semua data antrian dari depan ke belakang.
* Output Jumlah Antrian
Ketika memilih menu 5, program akan menampilkan jumlah pemohon yang masih berada dalam antrian.
* Output Keluar Program
Jika memilih menu 6, program akan berhenti dan menampilkan:

### Kesimpulan Output
* Output program menunjukkan bahwa sistem antrian berjalan sesuai konsep FIFO (First In First Out), di mana:
  * Data pertama yang masuk akan diproses terlebih dahulu
  * Penambahan terjadi di belakang antrian
  * Penghapusan terjadi di depan antrian

## e. Link YouTube
https://youtu.be/lKR1-4dvegw
