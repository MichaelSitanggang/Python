def fitur ():
    while True : 
        print("Pilih Fitur")
        print("1. Menentukan bilangan bulat positif atau negatif.")
        print("2. Menentukan suatu tahun adalah tahun kabisat atau bukan.")
        print("3. Menentukan kategori usia berdasarkan umur. ")
        print("4. Menentukan jumlah semua huruf dari sebuah kalimat ")
        print("5. Menentukan jumlah huruf dari sebuah kalimat ")
        print("6. Memasukkan Data nama kelas dan hobi")
        print("7. Keluar")
        pilih = int(input("Masukkan Pilihan : "))
        if (pilih == 1):
            bilangan()
        elif (pilih == 2):
            tahun()
        elif (pilih == 3):
            umur()
        elif(pilih == 7):
            print("Terimakasih hehe")
            break
        elif(pilih == 4):
            huruf()
        elif(pilih == 6):
            hasil()
        elif(pilih == 5):
            coba()
        ulangi = input("Mau ulang y/n : ")
        if (ulangi != 'y' ):
            print("Terimakasih telah mampir hehe")
            break

    
def bilangan():
    x = int(input("Bilangan : "))
    if (x < 0) :
        print("Bilangan negatif")
    elif (x == 0):
        print("Netral")
    else :
        print("Bilangan Positif")


def tahun():
    x = int(input("Masukkan Tahun : "))
    if (x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)):
        print("Tahun Kabisat")
    else :
        print("Bukan Tahun Kabisat")

def umur():
    x = int(input("Masukkan Umur : "))
    if (x == 0):
        print("Valid")
    elif (x<= 12):
        print("Anak - Anak")
    elif (x <= 18):
        print("Remaja")
    elif(x <= 59):
        print("Dewasa")
    else :
        print("Lansia")

def huruf():
    meghitung = input("Masukkan Kata : ")
    kata = len(meghitung)
    print(f"Jumlah Huruf : {kata}")

def coba():
    meghitung = input("Masukkan Kata : ")
    huruf = input("Huruf apa yang dihitung : ")
    hasil = meghitung.count(huruf)
    print(f"Huruf {huruf} Sebanyak : {hasil}")

def hasil():
    data = []
    n = int(input("Masukkan Jumlah Inputan : "))
    for i in range(n):
        nama = input("Masukkan Nama : ")
        kelas = input("Masukkan Kelas : ")
        hobi = input("Masukkan Hobi : ")
        print()

        data.append([nama,kelas,hobi])

    data.sort()
    for x in data :
        print(f"Nama : {x[0]} \nKelas : {x[1]} \nHobi : {x[2]}\n")
fitur()