# Implementasi Binary Search Tree pada Smart Fridge

## a. Judul Program

**Sistem Monitoring Makanan Berdasarkan Tanggal Kedaluwarsa Menggunakan Binary Search Tree (BST)**

## b. Deskripsi Singkat

Program ini merupakan implementasi struktur data **Binary Search Tree (BST)** dengan studi kasus **Smart Fridge** atau kulkas pintar. Program dibuat menggunakan bahasa Python untuk membantu mengelola data makanan berdasarkan tanggal kedaluwarsa.

Setiap makanan disimpan pada node BST dengan tanggal kedaluwarsa sebagai key utama. Data dengan tanggal kedaluwarsa yang lebih kecil akan ditempatkan pada subtree kiri, sedangkan data dengan tanggal yang lebih besar akan ditempatkan pada subtree kanan. Dengan demikian, data makanan dapat tersusun secara otomatis dan terurut berdasarkan waktu kedaluwarsa.

Operasi utama dalam program ini meliputi penambahan data makanan (*insert*), pencarian data makanan (*search*), menampilkan seluruh data secara terurut (*inorder*), mencari makanan yang paling cepat kedaluwarsa (*find_min*), mencari makanan yang paling lama kedaluwarsa (*find_max*), menghitung jumlah makanan (*count_nodes*), dan menghitung tinggi pohon (*height*).

## c. Source Code

### 1. Class Node

```python
class Node:
    def __init__(self, expired, nama):
        self.expired = expired
        self.nama = nama
        self.left = None
        self.right = None
```

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

```python
class SmartFridge:
    def __init__(self):
        self.root = None
```

- `class SmartFridge:`  
  Mendefinisikan class utama untuk mengelola BST.

- `def __init__(self):`  
  Constructor untuk inisialisasi BST.

- `self.root = None`  
  Menandakan bahwa BST masih kosong.

### 3. Fungsi insert_node()

```python
def insert_node(self, root, expired, nama):
    if root is None:
        return Node(expired, nama)

    if expired < root.expired:
        root.left = self.insert_node(root.left, expired, nama)
    elif expired > root.expired:
        root.right = self.insert_node(root.right, expired, nama)

    return root
```

- Fungsi ini digunakan untuk menambahkan node baru ke BST.
- Jika root kosong, maka node baru langsung dibuat.
- Jika tanggal kedaluwarsa lebih kecil dari root, maka data dimasukkan ke subtree kiri.
- Jika tanggal kedaluwarsa lebih besar dari root, maka data dimasukkan ke subtree kanan.
- Fungsi dilakukan secara rekursif sampai posisi yang sesuai ditemukan.

### 4. Fungsi insert()

```python
def insert(self, expired, nama):
    self.root = self.insert_node(self.root, expired, nama)
```

- Fungsi ini berfungsi sebagai pembungkus dari `insert_node()`.
- Digunakan untuk memulai proses penambahan data dari root.

### 5. Fungsi search_node()

```python
def search_node(self, root, expired):
    if root is None:
        return None

    if root.expired == expired:
        return root

    if expired < root.expired:
        return self.search_node(root.left, expired)

    return self.search_node(root.right, expired)
```

- Fungsi ini digunakan untuk mencari data makanan berdasarkan tanggal kedaluwarsa.
- Jika node kosong, maka data tidak ditemukan.
- Jika nilai yang dicari sama dengan key node, maka data ditemukan.
- Jika lebih kecil, pencarian dilakukan ke kiri.
- Jika lebih besar, pencarian dilakukan ke kanan.

### 6. Fungsi search()

```python
def search(self, expired):
    return self.search_node(self.root, expired)
```

- Fungsi ini digunakan untuk memulai pencarian dari root BST.

### 7. Fungsi inorder()

```python
def inorder(self, root):
    if root is None:
        return
    self.inorder(root.left)
    print(f"{root.expired} - {root.nama}")
    self.inorder(root.right)
```

- Fungsi ini menggunakan traversal inorder.
- Urutan traversal:
  1. Kunjungi subtree kiri.
  2. Tampilkan node saat ini.
  3. Kunjungi subtree kanan.
- Karena BST menyimpan nilai yang lebih kecil di kiri dan lebih besar di kanan, hasil inorder akan tampil terurut secara otomatis.

### 8. Fungsi find_min()

```python
def find_min(self, root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current
```

- Fungsi ini digunakan untuk mencari node dengan nilai terkecil.
- Pada BST, nilai terkecil selalu berada pada node paling kiri.
- Dalam studi kasus Smart Fridge, fungsi ini digunakan untuk mengetahui makanan yang paling cepat kedaluwarsa.

### 9. Fungsi find_max()

```python
def find_max(self, root):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right
    return current
```

- Fungsi ini digunakan untuk mencari node dengan nilai terbesar.
- Pada BST, nilai terbesar selalu berada pada node paling kanan.
- Dalam program ini, fungsi digunakan untuk mengetahui makanan yang paling lama kedaluwarsa.

### 10. Fungsi count_nodes()

```python
def count_nodes(self, root):
    if root is None:
        return 0
    return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
```

- Fungsi ini digunakan untuk menghitung jumlah seluruh node pada BST.
- Perhitungan dilakukan dengan menjumlahkan node saat ini, subtree kiri, dan subtree kanan.

### 11. Fungsi height()

```python
def height(self, root):
    if root is None:
        return -1

    height_left = self.height(root.left)
    height_right = self.height(root.right)
    return 1 + max(height_left, height_right)
```

- Fungsi ini digunakan untuk menghitung tinggi pohon BST.
- Tinggi pohon menunjukkan kedalaman maksimum struktur BST.

### 12. Fungsi main()

```python
def main():
```

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

Misalkan pengguna memasukkan data berikut:

| Tanggal Expired | Nama Makanan |
|-----------------|--------------|
| 20260530 | Susu UHT |
| 20260605 | Roti Tawar |
| 20260610 | Yogurt |
| 20260701 | Keju Cheddar |
| 20260815 | Saus Sambal |

BST yang terbentuk:

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

Ketika pengguna memilih menu **Tampilkan Makanan**, program menjalankan traversal inorder sehingga menghasilkan output:

```text
20260530 - Susu UHT
20260605 - Roti Tawar
20260610 - Yogurt
20260701 - Keju Cheddar
20260815 - Saus Sambal
```

Output tersebut menunjukkan bahwa BST berhasil mengurutkan data makanan berdasarkan tanggal kedaluwarsa dari yang paling cepat hingga yang paling lama.

Ketika pengguna memilih menu **Makanan Terdekat Kedaluwarsa**, program menjalankan fungsi `find_min()` sehingga menghasilkan output:

```text
Makanan terdekat kedaluwarsa:
20260530 - Susu UHT
```

Karena node tersebut merupakan nilai terkecil pada BST.

Ketika pengguna memilih menu **Makanan Paling Awet**, program menjalankan fungsi `find_max()` sehingga menghasilkan output:

```text
Makanan paling awet:
20260815 - Saus Sambal
```

Karena node tersebut merupakan nilai terbesar pada BST.

Ketika pengguna memilih menu **Jumlah Makanan**, program menghasilkan output:

```text
Jumlah makanan: 5
```

Karena terdapat lima node yang tersimpan pada BST.

## e. Kesimpulan

Program Smart Fridge merupakan implementasi Binary Search Tree (BST) yang digunakan untuk mengelola data makanan berdasarkan tanggal kedaluwarsa. Dengan BST, data dapat tersimpan secara terurut sehingga pengguna dapat mengetahui makanan yang harus segera dikonsumsi maupun makanan yang masih aman disimpan dalam waktu yang lama.

Melalui operasi *insert*, *search*, *inorder traversal*, *find_min*, *find_max*, *count_nodes*, dan *height*, program berhasil menunjukkan penerapan BST dalam menyelesaikan permasalahan nyata yang sering ditemui dalam kehidupan sehari-hari.

## f. Link YouTube

Link Video Presentasi : (Isi dengan link video presentasi Anda)
