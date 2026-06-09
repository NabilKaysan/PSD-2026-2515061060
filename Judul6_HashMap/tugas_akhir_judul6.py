class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nIsi Hash Table (Perpustakaan):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                buku = self.table[i].value
                print(
                    f"(Kode:{self.table[i].key}, "
                    f"Judul:{buku['judul']}, "
                    f"Penulis:{buku['penulis']})"
                )

def main():
    hashmap = HashMapOpenAddressing()

    while True:
        print("\n===== MENU PERPUSTAKAAN =====")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Hapus Buku")
        print("4. Tampilkan Semua Buku")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        try:
            if pilihan == "1":
                kode = int(input("Kode Buku : "))
                judul = input("Judul Buku : ")
                penulis = input("Penulis : ")
                data_buku = {
                    "judul": judul,
                    "penulis": penulis
                }
                if hashmap.insert(kode, data_buku):
                    print("Buku berhasil ditambahkan.")
                else:
                    print("Hash table penuh.")

            elif pilihan == "2":
                kode_cari = int(input("Masukkan kode buku yang dicari: "))
                hasil = hashmap.search(kode_cari)
                if hasil is not None:
                    buku = hasil.value
                    print("\nBuku ditemukan")
                    print("Kode Buku :", hasil.key)
                    print("Judul     :", buku["judul"])
                    print("Penulis   :", buku["penulis"])
                else:
                    print("\nBuku tidak ditemukan")

            elif pilihan == "3":
                kode_hapus = int(input("Masukkan kode buku yang akan dihapus: "))
                if hashmap.remove_key(kode_hapus):
                    print("Buku berhasil dihapus")
                else:
                    print("Buku tidak ditemukan")

            elif pilihan == "4":
                hashmap.display()
            elif pilihan == "5":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

if __name__ == "__main__":
    main()