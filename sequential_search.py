def squential_search(data, key):
    for item in data:
        if item == key:
            return True
    return False

my_list = [3, 6, 2, 9, 4, 7]
key = 6
found = squential_search(my_list, key)
if found:
    print("Elemen Ditemukan!!")
else:
    print("Elemen Tidak Ditemukan!!")