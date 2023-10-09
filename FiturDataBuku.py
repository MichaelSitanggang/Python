buku = []

def fitur():
    while True :
        print("Perpustakaan Michael")
        print("1. Menambah Buku")
        print("2. Melihat Buku")
        print("3. Menghapus Buku")
        print("4. Mengurutkan Nama Buku")
        print("5. Keluar")
        x = int(input("Masukkan Fitur Anda : "))
        if(x == 1):
            Menambah()
        elif(x == 2):
            melihat()
        elif(x == 3):
            menghapus()
        elif(x == 4):
            bubbleSort(buku)
            for index,value in enumerate(buku):
                print("")
                print(f"{index + 1}  |  {value[0]} \t | {value[1]} |")
        else : 
            break
        n = input("Apakah Mau Ulang (y/n) : ")
        if(n != 'y'):
            break
        
def Menambah():
    NamaBuku = input("Masukkan Nama Buku : ")
    Penulis  = input("Masukkan Nama Penulis : ")
    bukuBaru = [NamaBuku, Penulis]
    buku.append(bukuBaru)

def melihat():
        print("No |  Nama Buku  | Nama Penulis |")
        for index,value in enumerate(buku):
            print(f"{index + 1}  |  {value[0]} \t | {value[1]} |")

def menghapus():
    print("Daftar Buku")
    melihat()

    if not buku:
        print("Tidak Ada Buku yang dihapus")
        return

    hapusBuku = int(input("Menghapus Berdasarkan Index : ")) - 1
    if 0 <= hapusBuku < len(buku):
        buku_terhapus = buku.pop(hapusBuku)
        print(f"Buku '{buku_terhapus[0]}' telah dihapus.")
    else:
        print("Nomor buku tidak valid.")

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        hasil = False
        for j in range(0, n-i-1):
            if(arr[j][0] > arr[j+1][0]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                hasil = True
        if not hasil:
            break


fitur()