# Implementasi Queue Linked List pada Antrian Pesanan Kantin

## a. Judul Program

Sistem Antrian Pesanan Kantin Kampus

## b. Deskripsi Singkat

Program ini merupakan implementasi struktur data queue menggunakan singly linked list pada studi kasus antrian pesanan kantin kampus. Program dibuat menggunakan bahasa Python untuk mensimulasikan alur pemesanan makanan dan minuman yang diproses sesuai urutan kedatangan.

Struktur data yang digunakan adalah singly linked list, di mana setiap elemen (node) menyimpan data pesanan dan referensi ke node berikutnya. Sistem ini menerapkan konsep FIFO (First In First Out), yaitu pesanan yang masuk terlebih dahulu akan diproses terlebih dahulu.

Operasi utama dalam program ini meliputi:

* **enqueue**: menambahkan pesanan ke belakang antrian
* **dequeue**: memproses pesanan dari depan antrian
* **peek**: melihat pesanan terdepan tanpa menghapusnya
* **display**: menampilkan seluruh antrian pesanan
* **is_empty**: mengecek apakah antrian kosong

## c. Source Code

Kode program menggunakan dua class utama, yaitu `Node` dan `QueueLinkedList`.

### 1. Class Node

* `class Node:`
  Mendefinisikan class Node sebagai elemen dasar dalam linked list.
* `def __init__(self, data):`
  Constructor untuk menginisialisasi data pada node.
* `self.data = data`
  Menyimpan data pesanan.
* `self.next = None`
  Pointer ke node berikutnya, awalnya bernilai `None`.

### 2. Class QueueLinkedList

* `class QueueLinkedList:`
  Mendefinisikan class untuk mengelola sistem antrian pesanan kantin.
* `def __init__(self):`
  Constructor untuk inisialisasi antrian.
* `self.front_ptr = None`
  Menunjuk node pertama atau antrian terdepan.
* `self.rear_ptr = None`
  Menunjuk node terakhir atau antrian paling belakang.

### 3. Fungsi is_empty()

* `def is_empty(self):`
  Fungsi untuk mengecek apakah antrian kosong.
* `return self.front_ptr is None`
  Mengembalikan nilai `True` jika antrian kosong.

### 4. Fungsi enqueue()

* `def enqueue(self, x):`
  Fungsi untuk menambahkan data pesanan ke antrian.
* `new_node = Node(x)`
  Membuat node baru berisi data pesanan.
* `if self.is_empty():`
  Mengecek apakah antrian masih kosong.
* `self.front_ptr = new_node` dan `self.rear_ptr = new_node`
  Jika kosong, node baru menjadi node depan sekaligus node belakang.
* `else:`
  Jika antrian tidak kosong, node baru ditambahkan di belakang.
* `self.rear_ptr.next = new_node`
  Menghubungkan node terakhir dengan node baru.
* `self.rear_ptr = new_node`
  Memindahkan rear pointer ke node baru.
* `print("Pesanan berhasil masuk antrian.")`
  Menampilkan pesan bahwa pesanan berhasil ditambahkan.

### 5. Fungsi dequeue()

* `def dequeue(self):`
  Fungsi untuk menghapus data dari depan antrian.
* `if self.is_empty():`
  Mengecek apakah antrian kosong.
* `print("Antrian kosong")`
  Menampilkan pesan jika antrian tidak memiliki data.
* `return`
  Menghentikan proses fungsi.
* `temp = self.front_ptr`
  Menyimpan data pesanan yang akan diproses.
* `self.front_ptr = self.front_ptr.next`
  Memindahkan pointer depan ke node berikutnya.
* `if self.front_ptr is None:`
  Jika setelah penghapusan antrian menjadi kosong.
* `self.rear_ptr = None`
  Maka rear pointer juga dihapus.
* Menampilkan informasi pesanan yang sedang diproses, seperti nama, menu, dan catatan.

### 6. Fungsi peek()

* `def peek(self):`
  Fungsi untuk melihat data pada antrian terdepan tanpa menghapusnya.
* `if self.is_empty():`
  Mengecek apakah antrian kosong.
* `print("Antrian kosong")`
  Menampilkan pesan jika belum ada pesanan.
* Jika tidak kosong, program menampilkan pesanan yang berada di posisi paling depan.

### 7. Fungsi display()

* `def display(self):`
  Fungsi untuk menampilkan seluruh isi antrian.
* `if self.is_empty():`
  Mengecek apakah antrian kosong.
* `print("Antrian kosong")`
  Menampilkan pesan jika belum ada pesanan.
* `current = self.front_ptr`
  Menentukan node awal untuk proses penelusuran.
* `while current is not None:`
  Melakukan traversal sampai akhir antrian.
* Menampilkan seluruh pesanan dari depan ke belakang.

### 8. Fungsi main()

* `def main():`
  Fungsi utama program.
* `queue = QueueLinkedList()`
  Membuat objek queue.
* `pilih = 0`
  Variabel untuk menyimpan pilihan menu.
* `while pilih != 5:`
  Perulangan menu sampai pengguna memilih keluar.
* Program menampilkan menu utama:

  * Tambah pesanan
  * Proses pesanan
  * Lihat pesanan terdepan
  * Tampilkan semua antrian
  * Keluar

### 9. Percabangan Menu

* **Menu 1**
  Pengguna memasukkan nama pemesan, menu pesanan, dan catatan. Data tersebut disimpan ke dalam antrian menggunakan `enqueue()`.
* **Menu 2**
  Program memproses pesanan paling depan menggunakan `dequeue()`.
* **Menu 3**
  Program menampilkan pesanan terdepan menggunakan `peek()`.
* **Menu 4**
  Program menampilkan seluruh isi antrian menggunakan `display()`.
* **Menu 5**
  Program selesai.

### 10. Eksekusi Program

* `if __name__ == "__main__":`
  Menjalankan fungsi `main()` saat file dieksekusi langsung.

## d. Output Program

### Program akan menampilkan menu utama saat dijalankan

Saat program pertama kali dijalankan, pengguna akan melihat menu utama untuk mengelola antrian pesanan kantin.

### Penjelasan Output

* Ketika pengguna memilih **menu 1**, program akan meminta input:

  * Nama pemesan
  * Menu pesanan
  * Catatan pesanan

  Data yang dimasukkan akan ditempatkan di bagian belakang antrian sesuai prinsip FIFO.

* Ketika pengguna memilih **menu 2**, program akan memproses pesanan yang berada di bagian depan antrian.

* Ketika pengguna memilih **menu 3**, program akan menampilkan data pesanan terdepan tanpa menghapusnya.

* Ketika pengguna memilih **menu 4**, program akan menampilkan seluruh data pesanan dari depan ke belakang.

* Ketika pengguna memilih **menu 5**, program akan berhenti dan menampilkan pesan program selesai.

### Kesimpulan Output

Output program menunjukkan bahwa sistem antrian berjalan sesuai konsep **FIFO (First In First Out)**, di mana:

* pesanan yang masuk terlebih dahulu akan diproses terlebih dahulu,
* penambahan terjadi di belakang antrian,
* penghapusan terjadi di depan antrian.

## e. Kesimpulan

Program ini berhasil mengimplementasikan struktur data **Queue Linked List** dalam studi kasus antrian pesanan kantin kampus. Dengan adanya operasi `enqueue`, `dequeue`, `peek`, dan `display`, program dapat mensimulasikan proses antrian secara nyata dan sesuai dengan konsep FIFO.

## f. Link YouTube

(Bisa diisi jika sudah ada video presentasi atau demo program)
