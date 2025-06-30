#aplikasi sederhana pendataan gaji

# manager -> tunjangan 20%
# supervisior -> tunjangan 15%
# staff -> tunjangan 10%

gapok = 5000000
thp = []
data_karyawan = []
nama_jabatan = []

while True:
    nama = input("masukkan nama karyawan : ")
    jabatan = int(input("masukkan jabatan karyawan\n1. manager (1)\n2. supervisior (2)\n3. staff (3)\nmasukkan (1/2/3) : "))

    if jabatan == 1:
        thp = gapok * (20/100) + gapok
        nama_jabatan = "Manager"
    elif jabatan == 2:
        thp = gapok * (15/100) + gapok
        nama_jabatan = "Supervisior"
    elif jabatan == 3:
        thp = gapok * (10/100) + gapok
        nama_jabatan = "Staff"
    else:
        print("data tidak ditemukan !!!")
        
    data = [nama, nama_jabatan, gapok, thp]

    data_karyawan.append(data)
    
    print("-"*10,"Data Perusahaan",10*"-")
    print(f"No Nama Karyawan\t Jabatan\t Gaji")
    for index, data_perusahaan in enumerate(data_karyawan):
        print(f"{index+1} {data_perusahaan[0]}\t\t {data_perusahaan[1]}\t {data_perusahaan[3]}")
        
    lanjut = input("lanjutkan mengisi data (y/n) : ")
    
    if lanjut == "y":
        continue
    else:
        break
    
print("PROGRAM SELESAI !!!")
