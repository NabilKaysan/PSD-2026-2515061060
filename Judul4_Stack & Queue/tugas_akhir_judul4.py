class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        print("Pesanan berhasil masuk antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong")
            return

        temp = self.front_ptr
        print("Pesanan berikut berhasil diproses:")
        print(f"Nama   : {temp.data['nama']}")
        print(f"Menu   : {temp.data['menu']}")
        print(f"Catatan: {temp.data['catatan']}")
        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrian kosong")
            return

        print("Pesanan terdepan:")
        print(f"Nama   : {self.front_ptr.data['nama']}")
        print(f"Menu   : {self.front_ptr.data['menu']}")
        print(f"Catatan: {self.front_ptr.data['catatan']}")

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return

        print("Isi antrian pesanan (depan ke belakang):")
        current = self.front_ptr
        nomor = 1
        while current is not None:
            print(f"{nomor}. {current.data['nama']} - {current.data['menu']} - {current.data['catatan']}")
            current = current.next
            nomor += 1


def main():
    queue = QueueLinkedList()
    pilih = 0

    while pilih != 5:
        print("\n=== ANTRIAN PESANAN KANTIN ===")
        print("1. Tambah pesanan")
        print("2. Proses pesanan")
        print("3. Lihat pesanan terdepan")
        print("4. Tampilkan semua antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            nama = input("Nama pemesan: ")
            menu = input("Menu pesanan: ")
            catatan = input("Catatan: ")
            data = {
                "nama": nama,
                "menu": menu,
                "catatan": catatan
            }
            queue.enqueue(data)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()