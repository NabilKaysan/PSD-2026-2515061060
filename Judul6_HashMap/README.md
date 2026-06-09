# Implementasi Hash Map Open Addressing pada Sistem Perpustakaan

## a. Judul Program

Sistem Perpustakaan Menggunakan Hash Map Open Addressing

## b. Deskripsi Singkat

Program ini merupakan implementasi struktur data **Hash Map Open Addressing** menggunakan bahasa Python dengan studi kasus sistem perpustakaan. Program digunakan untuk menyimpan data buku berdasarkan kode buku yang dimasukkan oleh pengguna.

Struktur data yang digunakan adalah **Hash Map** dengan metode **Open Addressing (Linear Probing)** untuk menangani collision. Setiap buku memiliki kode buku sebagai **key** dan informasi buku berupa judul dan penulis sebagai **value**.

Operasi utama yang tersedia pada program meliputi penambahan buku (insert), pencarian buku (search), penghapusan buku (remove), dan menampilkan seluruh data buku yang tersimpan pada hash table (display).

---

## c. Source Code

### 1. Class SlotState
<img width="1000" height="576" alt="tugas_akhir_judul6 py" src="https://github.com/user-attachments/assets/c1f2dba6-a2fa-456d-b25e-90d0cce31f95" />

* `class SlotState:`

  * Digunakan untuk menyimpan status setiap slot pada hash table.

* `EMPTY = 0`

  * Menandakan slot masih kosong.

* `OCCUPIED = 1`

  * Menandakan slot sudah terisi data.

* `DELETED = 2`

  * Menandakan slot pernah digunakan tetapi datanya sudah dihapus.

---

### 2. Class Entry
<img width="1082" height="630" alt="tugas_akhir_judul6 py (1)" src="https://github.com/user-attachments/assets/412d8c5e-ad48-4b54-9d43-56d7fa77db05" />

* `class Entry:`

  * Digunakan untuk menyimpan data pada setiap slot hash table.

* `self.key`

  * Menyimpan kode buku.

* `self.value`

  * Menyimpan informasi buku.

* `self.state`

  * Menyimpan status slot.

---

### 3. Class HashMapOpenAddressing
<img width="1364" height="630" alt="tugas_akhir_judul6 py (2)" src="https://github.com/user-attachments/assets/9d5989f7-980a-4aa3-ab09-e7a19408c90a" />

* `class HashMapOpenAddressing:`

  * Class utama untuk mengelola hash table.

#### Constructor

* `def __init__(self, size=10):`

  * Digunakan untuk menginisialisasi ukuran hash table.

* `self.SIZE = size`

  * Menyimpan ukuran tabel.

* `self.table = [Entry() for _ in range(self.SIZE)]`

  * Membuat daftar slot kosong sebanyak ukuran tabel.

---

### 4. Fungsi hash_function()
<img width="1364" height="522" alt="tugas_akhir_judul6 py (3)" src="https://github.com/user-attachments/assets/6eaae2e3-68eb-48a2-8db2-d755b764e5c4" />

* `def hash_function(self, key):`

  * Digunakan untuk menentukan indeks penyimpanan berdasarkan key.

* `return (key % self.SIZE + self.SIZE) % self.SIZE`

  * Menghasilkan indeks hash yang valid.

---

### 5. Fungsi insert()
<img width="1364" height="1980" alt="tugas_akhir_judul6 py (4)" src="https://github.com/user-attachments/assets/7aa2d3aa-c56f-4cf3-b087-7e5598d6b922" />

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

### 6. Fungsi search()
<img width="1364" height="954" alt="tugas_akhir_judul6 py (5)" src="https://github.com/user-attachments/assets/23ce55a4-368d-4d56-aa26-ca06c93cd76a" />

* `def search(self, key):`

  * Digunakan untuk mencari data buku berdasarkan kode buku.

* `if self.table[i].state == SlotState.EMPTY`

  * Jika slot kosong maka data tidak ditemukan.

* `if self.table[i].key == key`

  * Jika key ditemukan maka data dikembalikan.

---

### 7. Fungsi remove_key()
<img width="1146" height="684" alt="tugas_akhir_judul6 py (6)" src="https://github.com/user-attachments/assets/836f9bda-d6fd-4219-8f87-1abaf8af50a9" />

* `def remove_key(self, key):`

  * Digunakan untuk menghapus data buku.

* `entry = self.search(key)`

  * Mencari data yang akan dihapus.

* `entry.state = SlotState.DELETED`

  * Mengubah status slot menjadi DELETED.

---

### 8. Fungsi display()
<img width="1364" height="1332" alt="tugas_akhir_judul6 py (7)" src="https://github.com/user-attachments/assets/ee3a80fa-7eba-40db-828e-54eac41ec628" />

* `def display(self):`

  * Digunakan untuk menampilkan seluruh isi hash table.

* `if self.table[i].state == SlotState.EMPTY`

  * Menampilkan status EMPTY.

* `elif self.table[i].state == SlotState.DELETED`

  * Menampilkan status DELETED.

* `else`

  * Menampilkan data buku yang tersimpan.

---

### 9. Fungsi main()
<img width="1364" height="4086" alt="tugas_akhir_judul6 py (8)" src="https://github.com/user-attachments/assets/7201b10e-737a-40ab-9263-6d830067ed43" />

* `def main():`

  * Fungsi utama program.

* `hashmap = HashMapOpenAddressing()`

  * Membuat objek hash map.

* `while True`

  * Menjalankan program secara berulang sampai pengguna memilih keluar.

* `try-except ValueError`

  * Menangani kesalahan input yang bukan angka.

---

### 10. Percabangan Menu

#### Tambah Buku

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

#### Cari Buku

* `elif pilihan == "2"`

  * Mencari data buku berdasarkan kode buku.

* Jika ditemukan maka program menampilkan:

  * Kode Buku
  * Judul Buku
  * Penulis

---

#### Hapus Buku

* `elif pilihan == "3"`

  * Menghapus buku berdasarkan kode buku.

* Status slot akan berubah menjadi DELETED.

---

#### Tampilkan Semua Buku

* `elif pilihan == "4"`

  * Menampilkan seluruh isi hash table.

---

#### Keluar Program

* `elif pilihan == "5"`

  * Menghentikan program.

---

### 11. Eksekusi Program

* `if __name__ == "__main__":`

  * Menjalankan fungsi `main()` saat file dieksekusi.

---

## d. Output Program

### Program akan menampilkan menu utama
<img width="340" height="192" alt="Screenshot 2026-06-09 202803" src="https://github.com/user-attachments/assets/dd7e8837-a30f-4277-ac6f-03cd78caf952" />


### Contoh Tambah Buku

Input:

<img width="270" height="91" alt="Screenshot 2026-06-09 202918" src="https://github.com/user-attachments/assets/ca15d17d-1510-4838-9147-ff987b9fe21a" />


Output:

<img width="293" height="36" alt="Screenshot 2026-06-09 202924" src="https://github.com/user-attachments/assets/1fb37752-012d-4ea0-9235-f2c1beeb80a6" />


### Contoh Cari Buku

Input:

<img width="372" height="58" alt="Screenshot 2026-06-09 202951" src="https://github.com/user-attachments/assets/7faeb83a-eb93-47f6-9cc3-88a75c9ca199" />


Output:

<img width="286" height="101" alt="Screenshot 2026-06-09 202955" src="https://github.com/user-attachments/assets/43f928b2-64bc-4259-b760-9369da54b4d1" />


### Contoh Hapus Buku

Input:

<img width="401" height="47" alt="Screenshot 2026-06-09 203049" src="https://github.com/user-attachments/assets/369845c5-e17a-4c9e-aa2e-d30242d7aaa7" />


Output:

<img width="245" height="25" alt="Screenshot 2026-06-09 203054" src="https://github.com/user-attachments/assets/85af2a41-65ae-472a-915d-eb52dc2865d5" />


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
