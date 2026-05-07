def sequential_search(slot_parkir, n, target):
    i = 0
    counter = 0
    posisi = []
    while i < n:
        if slot_parkir[i][1].lower() == target.lower():
            counter += 1
            posisi.append(i)
        i += 1
    return counter, posisi


def main():
    slot_parkir = [
        ["A01", "Terisi", "1A", "Mobil"],
        ["A02", "Terisi", "1A", "Mobil"],
        ["A03", "Kosong", "2A", "Mobil"],
        ["A04", "Terisi", "2B", "Motor"],
        ["A05", "Kosong", "3A", "Mobil"],
        ["A06", "Terisi", "3B", "Motor"],
        ["A07", "Kosong", "4A", "Mobil"]
    ]

    n = len(slot_parkir)

    print("Data slot parkir:")
    for data in slot_parkir:
        print(f"{data[0]} | {data[1]} | Lantai {data[2]} | {data[3]}")

    while True:
        try:
            target = input("\nMasukkan status yang dicari (Kosong/Terisi): ")
            if target.strip() == "":
                print("Input tidak boleh kosong!")
            else:
                break
        except ValueError:
            print("Input tidak valid!")

    counter, posisi = sequential_search(slot_parkir, n, target)

    if counter > 0:
        print(f"\nStatus {target} ditemukan sebanyak {counter} kali.")
        for p in posisi:
            print(f"Indeks ke-{p}")
            print(f"Kode Slot : {slot_parkir[p][0]}")
            print(f"Status    : {slot_parkir[p][1]}")
            print(f"Lantai    : {slot_parkir[p][2]}")
            print(f"Jenis     : {slot_parkir[p][3]}\n")
    else:
        print(f"\nStatus {target} tidak ditemukan.")


if __name__ == "__main__":
    main()