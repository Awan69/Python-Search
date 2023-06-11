def cari_nomer(nama, buku_telpon):
    for kontak_nama, nomer in buku_telpon.items():
        if kontak_nama == nama:
            return nomer
    return None


buku_telpon = {
    "John Doe": "081234567890",
    "Jane Smith": "089876543210",
    "Michael Johnson": "087811223344",
    "Emily Davis": "082122232425"
}

nama = "Jane Smith"

nomer = cari_nomer(nama, buku_telpon)

if nomer:
    print("Nomor telepon", nama, "adalah", nomer)
else:
    print("Nomor telepon", nama, "tidak ditemukan.")
