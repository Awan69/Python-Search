def binary_search_insertion(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return mid

        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


data = [2, 4, 6, 8, 10, 12, 14]
target = 7

insertion_index = binary_search_insertion(data, target)

print("Elemen", target, "dapat disisipkan pada indeks",
      insertion_index, "untuk menjaga daftar tetap terurut.")
