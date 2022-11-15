import time, os

def garis1():
    print("="*70)

def garis2():
    print("-"*70)

def menu1():
    print()
    print("I BOX".center(54)) 
    print("-"*54)
    print("| KODE |        NAMA BARANG        |       HARGA     |")
    print("-"*54)
    print("|   1  |  IPhone 14 Pro Max 128GB  |  Rp 25.000.000  |")
    print("|   2  |  IPhone 13 Pro Max 128GB  |  Rp 19.000.000  |")
    print("|   3  |  IPhone 12 Pro Max 128GB  |  Rp 16.000.000  |")
    print("|   4  |  IPhone SE 3rd Gen 128GB  |  Rp 10.000.000  |")
    print("-"*54)

def menu2():
    print(" NO |       NAMA BARANG       |   HARGA/PCS  | QTY |     SUBTOTAL      ")
    garis2()

def head():
    print()
    print("IBox".center(70))
    print("IBOX PENDAWA BARU CENTER".center(70))
    print("JL. CIPENDAWA BARU NO.199, BEKASI, JAWA BARAT".center(70))
    print("Telp : 0838-1709-7070".center(70))
    print()
    localtime = time.asctime( time.localtime(time.time()) )
    print("Tanggal \t:",localtime) 
    print("Pelayan/Kasir \t:",kasir)
    print("Nama Pembeli \t:", np)
    garis1()

print()
kasir=input("masukkan nama kasir : ")
pilihan="y"
while pilihan=="y":
    os.system('cls')
    menu1()
    np=input("Nama Pembeli \t : ")
    jb=int(input("Jumlah Transaksi : "))
    kb=[]
    nb=[]
    mj=[]
    tb=[]
    ub=[]
    uk=[]
    h=[]
    j=[]
    i=0
    while i<jb:
        print("\ndata ke-",i+1)

        kb.append(int(input("Masukkan Kode Barang : ")))
        mj.append(int(input("Masukkan Jumlah Beli : ")))
        if kb[i] == 1:
            nb.append("IPhone 14 Pro Max 128GB")
            h.append("25.000.000")
            j.append(mj[i]*int(25000000))
        elif kb[i] == 2:
            nb.append("IPhone 13 Pro Max 128GB")
            h.append("19.000.000")
            j.append(mj[i]*int(19000000))
        elif kb[i] == 3:
            nb.append("IPhone 12 Pro Max 128GB")
            h.append("16.000.000")
            j.append(mj[i]*int(17000000))
        elif kb[i] == 4:
            nb.append("IPhone SE 3rd GEN 128GB")
            h.append("10.000.000")
            j.append(mj[i]*int(10000000))
        else: 
            nb.append("Kode Salah")
            h.append("0")
            j.append(mj[i]*int(0))
        i=i+1

    os.system("cls")
    head()
    menu2()
    tb=0
    a=0
    while a<jb:
        tb=tb+j[a]
        print("  %i   %s    %s     %i       %i"%(a+1, nb[a], h[a], mj[a], j[a]))
        a=a+1
    garis2()
    print("Total Belanjaan : Rp",tb)
    b=int(input("Uang Dibayarkan : Rp "))
    uk=b-tb
    print("Uang Kembali \t: Rp",uk)
    garis1()
    print("! Barang yang sudah dibeli tidak dapat ditukar/dikembalikan !".center(70))
    print("TERIMA KASIH - THANK YOU".center(70))
    print()
    print()
    print()
    print()
    pilihan=input("Pesanan Lain (y/n) : ")