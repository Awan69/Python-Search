def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()

    if title1[0] == title2[0]:
        return True
    
    return False

def seqeuential_search(book, book_title):
    for book in book :
        if is_similar(book['title'], book_title):
            return book['shelf']
        
        return "Buku Tidak Ditemukan."
    
book = [
    {'title' : 'Python Programing', 'shelf' : 'A1'},
    {'title' : 'Struktur Data dan Algoritma', 'shelf' : 'B2'},
    {'title' : 'Perkenalan Machine Learning', 'shelf' : 'C3'},
    {'title' : 'Database Managment System', 'shelf' : 'D4'}
]

book_title = input("Masukan judul biku yang ingin dicari: ")
shelf_location = seqeuential_search(book, book_title)
print(shelf_location)