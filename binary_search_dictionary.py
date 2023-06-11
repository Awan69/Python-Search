def cari_definisi(kamus, kata):
    left = 0
    right = len(kamus) - 1

    while left <= right:
        mid = (left + right) // 2

        if kamus[mid][0] == kata:
            return kamus[mid]

        if kamus[mid][0] < kata:
            left = mid + 1
        else:
            right = mid - 1

    return None


kamus = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

print("Kata:")
for kata_definisi in kamus:
    print(kata_definisi[0])

kata = input("Masukkan kata yang ingin dicari definisinya: ")

definisi = cari_definisi(kamus, kata)

if definisi:
    print("Kata:", definisi[0])
    print("Definisi:", definisi[1])
else:
    print("Kata", kata, "tidak ditemukan dalam kamus.")
