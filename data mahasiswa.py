#aplikasi sederhana pendataan nilai mahasiswa


nilai = []
status = []
while True:
    nama = input("masukkan nama mahasiswa : ")
    nim = int(input("masukkan NIM mahasiswa : "))
    nilai_mahasiswa = int(input("masukkan nilai mahasiswa : "))
    
    if nilai_mahasiswa < 70:
        status = "Tidak Lulus"
    elif nilai_mahasiswa == 70:
        status = "remidial"
    elif nilai_mahasiswa > 70:
        status = "Lulus"
    else:
        status = "data tidak ditemukan"

    data = [nama, nim, nilai_mahasiswa, status]

    nilai.append(data)

    print("-"*7,"DATA", 7*"-")
    print(f"Nama\t NIM\t Nilai")
    for mahasiswa in nilai:
        print(f"{mahasiswa[0]}\t {mahasiswa[1]}\t {mahasiswa[2]}\t {mahasiswa[3]}")
        
        
    islanjut = input("lanjutkan isi data (y/n) : ")
    
    if islanjut == "y":
        continue
    else:
        break

print("kode selesai !!!")
    

