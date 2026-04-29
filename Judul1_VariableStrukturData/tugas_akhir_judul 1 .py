class Node:
    def __init__(self, nomor, nama, jenis_sim):
        self.nomor = nomor
        self.nama = nama
        self.jenis_sim = jenis_sim
        self.next = None


class AntrianSIM:
    def __init__(self):
        self.head = None
        self.tail = None
        self.total = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, nama, jenis_sim):
        self.total += 1
        node_baru = Node(self.total, nama, jenis_sim)

        if self.is_empty():
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru

        print(f"Antrian berhasil ditambahkan. Nomor antrian: {node_baru.nomor}")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada peserta yang bisa dilayani.")
            return

        data_keluar = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        print("\n=== PELAYANAN SIM ===")
        print(f"Nomor Antrian : {data_keluar.nomor}")
        print(f"Nama          : {data_keluar.nama}")
        print(f"Jenis SIM     : {data_keluar.jenis_sim}")
        print("Status        : Telah dilayani")

    def peek(self):
        if self.is_empty():
            print("Antrian masih kosong.")
        else:
            print("\nAntrian terdepan:")
            print(f"Nomor Antrian : {self.head.nomor}")
            print(f"Nama          : {self.head.nama}")
            print(f"Jenis SIM     : {self.head.jenis_sim}")

    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
            return

        print("\n=== DAFTAR ANTRIAN PELAYANAN SIM ===")
        current = self.head
        while current is not None:
            print(f"[{current.nomor}] {current.nama} - SIM {current.jenis_sim}")
            current = current.next

    def jumlah_antrian(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print(f"Jumlah antrian saat ini: {count}")


def menu():
    print("\n===== MENU ANTRIAN PELAYANAN SIM =====")
    print("1. Tambah antrian")
    print("2. Layani antrian")
    print("3. Lihat antrian terdepan")
    print("4. Tampilkan seluruh antrian")
    print("5. Jumlah antrian")
    print("6. Keluar")


def main():
    antrian = AntrianSIM()

    while True:
        menu()
        try:
            pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka.")
            continue

        if pilihan == 1:
            nama = input("Masukkan nama pemohon: ").strip()
            jenis_sim = input("Masukkan jenis SIM (A/C/D): ").strip().upper()

            if nama == "":
                print("Nama tidak boleh kosong.")
                continue

            if jenis_sim not in ["A", "C", "D"]:
                print("Jenis SIM harus A, C, atau D.")
                continue

            antrian.enqueue(nama, jenis_sim)

        elif pilihan == 2:
            antrian.dequeue()

        elif pilihan == 3:
            antrian.peek()

        elif pilihan == 4:
            antrian.display()

        elif pilihan == 5:
            antrian.jumlah_antrian()

        elif pilihan == 6:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
