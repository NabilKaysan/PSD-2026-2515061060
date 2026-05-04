def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def hitung_skor(masakan):
    return masakan[1] + masakan[2]


def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and hitung_skor(arr[j]) < hitung_skor(temp):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah masakan: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan data masakan:")

    for i in range(n):
        while True:
            try:
                nama = input("Nama masakan: ")
                waktu = int(input("Waktu masak (menit): "))
                sulit = int(input("Tingkat kesulitan (1-100): "))
                target = int(input("Target waktu siap (menit): "))

                arr.append([nama, waktu, sulit, target])
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka yang benar!")

    print("\nData sebelum diurutkan:")
    for i in range(n):
        print(arr[i])

    insertion_sort(arr, n)

    print("\nUrutan memasak yang disarankan:")
    for i in range(n):
        print(f"{arr[i][0]} (Skor: {hitung_skor(arr[i])})")


if __name__ == "__main__":
    main()