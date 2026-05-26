class Node:
    def __init__(self, expired, nama):
        self.expired = expired
        self.nama = nama
        self.left = None
        self.right = None


class SmartFridge:
    def __init__(self):
        self.root = None

    def insert_node(self, root, expired, nama):
        if root is None:
            return Node(expired, nama)

        if expired < root.expired:
            root.left = self.insert_node(root.left, expired, nama)
        elif expired > root.expired:
            root.right = self.insert_node(root.right, expired, nama)

        return root

    def insert(self, expired, nama):
        self.root = self.insert_node(self.root, expired, nama)

    def search_node(self, root, expired):
        if root is None:
            return None

        if root.expired == expired:
            return root

        if expired < root.expired:
            return self.search_node(root.left, expired)

        return self.search_node(root.right, expired)

    def search(self, expired):
        return self.search_node(self.root, expired)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(f"{root.expired} - {root.nama}")
        self.inorder(root.right)

    def find_min(self, root):
        if root is None:
            return None

        current = root
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, root):
        if root is None:
            return None

        current = root
        while current.right is not None:
            current = current.right
        return current

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def height(self, root):
        if root is None:
            return -1

        height_left = self.height(root.left)
        height_right = self.height(root.right)
        return 1 + max(height_left, height_right)


def main():
    fridge = SmartFridge()
    pilih = 0

    while pilih != 8:
        print("\n=== SMART FRIDGE BST ===")
        print("1. Tambah Makanan")
        print("2. Cari Makanan")
        print("3. Tampilkan Makanan")
        print("4. Makanan Terdekat Kedaluwarsa")
        print("5. Makanan Paling Awet")
        print("6. Jumlah Makanan")
        print("7. Tinggi Pohon")
        print("8. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                expired = int(input("Tanggal expired (yyyymmdd): "))
                nama = input("Nama makanan: ")
                fridge.insert(expired, nama)
                print("Makanan berhasil ditambahkan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                expired = int(input("Cari tanggal expired: "))
                hasil = fridge.search(expired)

                if hasil is not None:
                    print(f"Ditemukan: {hasil.expired} - {hasil.nama}")
                else:
                    print("Data tidak ditemukan")
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("\nDaftar Makanan:")
            fridge.inorder(fridge.root)

        elif pilih == 4:
            data = fridge.find_min(fridge.root)
            if data is not None:
                print(f"Makanan terdekat kedaluwarsa: {data.expired} - {data.nama}")
            else:
                print("Data masih kosong")

        elif pilih == 5:
            data = fridge.find_max(fridge.root)
            if data is not None:
                print(f"Makanan paling awet: {data.expired} - {data.nama}")
            else:
                print("Data masih kosong")

        elif pilih == 6:
            print(f"Jumlah makanan: {fridge.count_nodes(fridge.root)}")

        elif pilih == 7:
            print(f"Tinggi pohon: {fridge.height(fridge.root)}")

        elif pilih == 8:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()