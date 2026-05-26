# Implementasi Binary Search Tree pada Smart Fridge

## A. Judul Program

**Sistem Monitoring Makanan Berdasarkan Tanggal Kedaluwarsa Menggunakan Binary Search Tree (BST)**

---

## B. Deskripsi Program

Program Smart Fridge merupakan implementasi struktur data Binary Search Tree (BST) yang digunakan untuk mengelola data makanan berdasarkan tanggal kedaluwarsa. Setiap makanan memiliki tanggal kedaluwarsa sebagai key utama dan nama makanan sebagai data yang disimpan pada node BST.

Dengan menggunakan BST, data makanan dapat tersusun secara otomatis berdasarkan tanggal kedaluwarsa. Hal ini memudahkan pengguna untuk mengetahui makanan yang harus segera dikonsumsi maupun makanan yang masih dapat disimpan dalam waktu yang lama.

Fitur yang tersedia dalam program ini adalah:

- Menambahkan makanan.
- Mencari makanan berdasarkan tanggal kedaluwarsa.
- Menampilkan seluruh makanan secara terurut.
- Menampilkan makanan yang paling cepat kedaluwarsa.
- Menampilkan makanan yang paling lama kedaluwarsa.
- Menghitung jumlah makanan.
- Menghitung tinggi BST.

---

## C. Source Code

### 1. Class Node

```python
class Node:
    def __init__(self, expired, nama):
        self.expired = expired
        self.nama = nama
        self.left = None
        self.right = None
```

Class `Node` digunakan untuk membentuk node pada BST. Setiap node menyimpan tanggal kedaluwarsa (`expired`) sebagai key, nama makanan (`nama`), serta pointer menuju anak kiri (`left`) dan anak kanan (`right`).

### 2. Class SmartFridge

```python
class SmartFridge:
    def __init__(self):
        self.root = None
```

Class `SmartFridge` digunakan untuk mengelola seluruh operasi BST. Variabel `root` berfungsi sebagai akar pohon dan bernilai `None` ketika BST masih kosong.

### 3. Fungsi insert_node()

```python
def insert_node(self, root, expired, nama):
```

Fungsi ini digunakan untuk menambahkan node baru ke dalam BST.

Cara kerja fungsi:

- Jika node kosong maka dibuat node baru.
- Jika tanggal kedaluwarsa lebih kecil dari root maka data dimasukkan ke subtree kiri.
- Jika tanggal kedaluwarsa lebih besar dari root maka data dimasukkan ke subtree kanan.
- Proses dilakukan secara rekursif hingga posisi yang sesuai ditemukan.

### 4. Fungsi insert()

```python
def insert(self, expired, nama):
    self.root = self.insert_node(self.root, expired, nama)
```

Fungsi ini digunakan untuk memanggil fungsi `insert_node()` sehingga proses penambahan data dimulai dari root BST.

### 5. Fungsi search_node()

```python
def search_node(self, root, expired):
```

Fungsi ini digunakan untuk mencari data makanan berdasarkan tanggal kedaluwarsa.

Proses pencarian dilakukan dengan membandingkan nilai yang dicari dengan key pada node saat ini.

- Jika lebih kecil maka bergerak ke kiri.
- Jika lebih besar maka bergerak ke kanan.
- Jika sama maka data ditemukan.

### 6. Fungsi search()

```python
def search(self, expired):
    return self.search_node(self.root, expired)
```

Fungsi ini digunakan untuk memulai proses pencarian dari root BST.

### 7. Fungsi inorder()

```python
def inorder(self, root):
```

Fungsi ini menggunakan metode Inorder Traversal.

Urutan prosesnya adalah:

1. Mengunjungi subtree kiri.
2. Menampilkan data node saat ini.
3. Mengunjungi subtree kanan.

Karena BST menyimpan data lebih kecil di kiri dan lebih besar di kanan, hasil traversal akan tampil secara terurut.

### 8. Fungsi find_min()

```python
def find_min(self, root):
```

Fungsi ini digunakan untuk mencari node dengan nilai terkecil pada BST.

Dalam studi kasus Smart Fridge, fungsi ini digunakan untuk mengetahui makanan yang paling cepat kedaluwarsa sehingga harus segera dikonsumsi.

### 9. Fungsi find_max()

```python
def find_max(self, root):
```

Fungsi ini digunakan untuk mencari node dengan nilai terbesar pada BST.

Dalam program ini fungsi digunakan untuk mengetahui makanan yang memiliki masa simpan paling lama.

### 10. Fungsi count_nodes()

```python
def count_nodes(self, root):
```

Fungsi ini digunakan untuk menghitung jumlah seluruh node yang ada pada BST.

Proses perhitungan dilakukan dengan menjumlahkan node saat ini, subtree kiri, dan subtree kanan.

### 11. Fungsi height()

```python
def height(self, root):
```

Fungsi ini digunakan untuk menghitung tinggi pohon BST.

Nilai height menunjukkan kedalaman maksimum pohon yang terbentuk.

### 12. Fungsi main()

```python
def main():
```

Fungsi utama program yang digunakan untuk:

- Menampilkan menu.
- Menerima input pengguna.
- Menjalankan operasi BST sesuai pilihan menu.
- Mengakhiri program ketika pengguna memilih keluar.

---

## D. Penjelasan Output

Misalkan pengguna memasukkan data berikut:

| Tanggal Expired | Nama Makanan |
|---------------|--------------|
| 20260530 | Susu UHT |
| 20260605 | Roti Tawar |
| 20260610 | Yogurt |
| 20260701 | Keju Cheddar |
| 20260815 | Saus Sambal |

BST yang terbentuk adalah:

```text
20260530
      \
    20260605
          \
        20260610
              \
            20260701
                  \
                20260815
```

Ketika pengguna memilih menu **Tampilkan Makanan**, program akan menjalankan traversal inorder sehingga menghasilkan output:

```text
20260530 - Susu UHT
20260605 - Roti Tawar
20260610 - Yogurt
20260701 - Keju Cheddar
20260815 - Saus Sambal
```

Output tersebut menunjukkan bahwa BST berhasil mengurutkan data makanan berdasarkan tanggal kedaluwarsa dari yang paling cepat hingga yang paling lama.

Ketika pengguna memilih menu **Makanan Terdekat Kedaluwarsa**, program menjalankan fungsi `find_min()` sehingga menghasilkan:

```text
Makanan terdekat kedaluwarsa:
20260530 - Susu UHT
```

Karena node tersebut merupakan nilai terkecil pada BST.

Ketika pengguna memilih menu **Makanan Paling Awet**, program menjalankan fungsi `find_max()` sehingga menghasilkan:

```text
Makanan paling awet:
20260815 - Saus Sambal
```

Karena node tersebut merupakan nilai terbesar pada BST.

Ketika pengguna memilih menu **Jumlah Makanan**, program menghasilkan:

```text
Jumlah makanan: 5
```

Karena terdapat lima node yang tersimpan pada BST.

---

## E. Kesimpulan

Program Smart Fridge merupakan implementasi Binary Search Tree (BST) yang digunakan untuk mengelola data makanan berdasarkan tanggal kedaluwarsa. Dengan BST, data dapat tersimpan secara terurut sehingga pengguna dapat mengetahui makanan yang harus segera dikonsumsi maupun makanan yang masih aman disimpan dalam waktu yang lama.

Melalui operasi insert, search, inorder traversal, find_min, find_max, count_nodes, dan height, program berhasil menunjukkan penerapan BST dalam menyelesaikan permasalahan nyata yang sering ditemui dalam kehidupan sehari-hari.
