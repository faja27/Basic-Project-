#aplikasi sederhana pendataan buku


data_buku = []
while True:
    judul =  input("masukkan judul buku : ")
    penulis = input("masukkan nama penulis : ")

    buku = [judul, penulis]
    
    data_buku.append(buku)
    
    print("-"*10, "DATA BUKU", "-"*10)
    print(f"No\t judul buku \t\t Penulis buku")
    
    for index, books in enumerate(data_buku):
        print(f"{index+1}\t {books[0]}\t\t {books[1]}")
        
    
    islanjut = input("apakah lanjut menginput data (y/n) ? ")
    
    if islanjut == "y":
        continue
    else:
        break
    
print("Aplikasi selesai !!!")
        
    
