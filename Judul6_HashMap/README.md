# Implementasi Hash Map Open Addressing pada Sistem Perpustakaan

## a. Judul Program

Sistem Perpustakaan Menggunakan Hash Map Open Addressing

## b. Deskripsi Singkat

Program ini merupakan implementasi struktur data **Hash Map Open Addressing** menggunakan bahasa Python dengan studi kasus sistem perpustakaan. Program digunakan untuk menyimpan data buku berdasarkan kode buku yang dimasukkan oleh pengguna.

Struktur data yang digunakan adalah **Hash Map** dengan metode **Open Addressing (Linear Probing)** untuk menangani collision. Setiap buku memiliki kode buku sebagai **key** dan informasi buku berupa judul dan penulis sebagai **value**.

Operasi utama yang tersedia pada program meliputi penambahan buku (insert), pencarian buku (search), penghapusan buku (remove), dan menampilkan seluruh data buku yang tersimpan pada hash table (display).

---

# c. Source Code

## 1. Class SlotState

* `class SlotState:`

  * Digunakan untuk menyimpan status setiap slot pada hash table.

* `EMPTY = 0`

  * Menandakan slot masih kosong.

* `OCCUPIED = 1`

  * Menandakan slot sudah terisi data.

* `DELETED = 2`

  * Menandakan slot pernah digunakan tetapi datanya sudah dihapus.

---

## 2. Class Entry

* `class Entry:`

  * Digunakan untuk menyimpan data pada setiap slot hash table.

* `self.key`

  * Menyimpan kode buku.

* `self.value`

  * Menyimpan informasi buku.

* `self.state`

  * Menyimpan status slot.

---

## 3. Class HashMapOpenAddressing

* `class HashMapOpenAddressing:`

  * Class utama untuk mengelola hash table.

### Constructor

* `def __init__(self, size=10):`

  * Digunakan untuk menginisialisasi ukuran hash table.

* `self.SIZE = size`

  * Menyimpan ukuran tabel.

* `self.table = [Entry() for _ in range(self.SIZE)]`

  * Membuat daftar slot kosong sebanyak ukuran tabel.

---

## 4. Fungsi hash_function()

* `def hash_function(self, key):`

  * Digunakan untuk menentukan indeks penyimpanan berdasarkan key.

* `return (key % self.SIZE + self.SIZE) % self.SIZE`

  * Menghasilkan indeks hash yang valid.

---

## 5. Fungsi insert()

* `def insert(self, key, value):`

  * Digunakan untuk menambahkan data buku ke hash table.

* `idx = self.hash_function(key)`

  * Menentukan indeks awal berdasarkan key.

* `for step in range(self.SIZE):`

  * Melakukan proses linear probing.

* `if self.table[i].state == SlotState.OCCUPIED`

  * Mengecek apakah slot sudah terisi.

* `if self.table[i].key == key`

  * Jika key sudah ada maka data lama diperbarui.

* `elif self.table[i].state == SlotState.DELETED`

  * Menyimpan posisi slot yang pernah dihapus.

* `self.table[i].key = key`

  * Menyimpan kode buku.

* `self.table[i].value = value`

  * Menyimpan data buku.

* `self.table[i].state = SlotState.OCCUPIED`

  * Mengubah status slot menjadi terisi.

---

## 6. Fungsi search()

* `def search(self, key):`

  * Digunakan untuk mencari data buku berdasarkan kode buku.

* `if self.table[i].state == SlotState.EMPTY`

  * Jika slot kosong maka data tidak ditemukan.

* `if self.table[i].key == key`

  * Jika key ditemukan maka data dikembalikan.

---

## 7. Fungsi remove_key()

* `def remove_key(self, key):`

  * Digunakan untuk menghapus data buku.

* `entry = self.search(key)`

  * Mencari data yang akan dihapus.

* `entry.state = SlotState.DELETED`

  * Mengubah status slot menjadi DELETED.

---

## 8. Fungsi display()

* `def display(self):`

  * Digunakan untuk menampilkan seluruh isi hash table.

* `if self.table[i].state == SlotState.EMPTY`

  * Menampilkan status EMPTY.

* `elif self.table[i].state == SlotState.DELETED`

  * Menampilkan status DELETED.

* `else`

  * Menampilkan data buku yang tersimpan.

---

## 9. Fungsi main()

* `def main():`

  * Fungsi utama program.

* `hashmap = HashMapOpenAddressing()`

  * Membuat objek hash map.

* `while True`

  * Menjalankan program secara berulang sampai pengguna memilih keluar.

* `try-except ValueError`

  * Menangani kesalahan input yang bukan angka.

---

## 10. Percabangan Menu

### Tambah Buku

* `if pilihan == "1"`

  * Menambahkan data buku ke hash table.

* Pengguna memasukkan:

  * Kode Buku
  * Judul Buku
  * Penulis

* Data disimpan dalam dictionary:

```python
{
    "judul": judul,
    "penulis": penulis
}
```

---

### Cari Buku

* `elif pilihan == "2"`

  * Mencari data buku berdasarkan kode buku.

* Jika ditemukan maka program menampilkan:

  * Kode Buku
  * Judul Buku
  * Penulis

---

### Hapus Buku

* `elif pilihan == "3"`

  * Menghapus buku berdasarkan kode buku.

* Status slot akan berubah menjadi DELETED.

---

### Tampilkan Semua Buku

* `elif pilihan == "4"`

  * Menampilkan seluruh isi hash table.

---

### Keluar Program

* `elif pilihan == "5"`

  * Menghentikan program.

---

## 11. Eksekusi Program

* `if __name__ == "__main__":`

  * Menjalankan fungsi `main()` saat file dieksekusi.

---

# d. Output Program

### Program akan menampilkan menu utama

```text
===== MENU PERPUSTAKAAN =====
1. Tambah Buku
2. Cari Buku
3. Hapus Buku
4. Tampilkan Semua Buku
5. Keluar
```

### Contoh Tambah Buku

```text
Kode Buku : 101
Judul Buku : Python Dasar
Penulis : Andi
```

Output:

```text
Buku berhasil ditambahkan.
```

### Contoh Cari Buku

Input:

```text
Masukkan kode buku yang dicari: 101
```

Output:

```text
Buku ditemukan
Kode Buku : 101
Judul     : Python Dasar
Penulis   : Andi
```

### Contoh Hapus Buku

Input:

```text
Masukkan kode buku yang akan dihapus: 101
```

Output:

```text
Buku berhasil dihapus
```

---

## Penjelasan Output

* Ketika pengguna memilih menu Tambah Buku, data buku akan disimpan ke dalam hash table menggunakan kode buku sebagai key.

* Ketika pengguna memilih menu Cari Buku, program akan melakukan pencarian berdasarkan key menggunakan teknik linear probing.

* Ketika pengguna memilih menu Hapus Buku, data tidak langsung dihilangkan dari tabel, tetapi statusnya diubah menjadi DELETED.

* Ketika pengguna memilih menu Tampilkan Semua Buku, seluruh isi hash table akan ditampilkan beserta status setiap slot.

---

## Kesimpulan Output

Output program menunjukkan bahwa implementasi Hash Map Open Addressing dapat digunakan untuk mengelola data buku pada sistem perpustakaan. Teknik Linear Probing memungkinkan collision ditangani dengan mencari slot kosong berikutnya sehingga proses penyimpanan dan pencarian data tetap berjalan dengan baik.

---

# e. Link YouTube

https://youtube.com/

(Ganti dengan link video demonstrasi program Anda)
