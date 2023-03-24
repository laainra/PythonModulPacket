from luas.lingkaran import *
from luas.jajargenjang import *
from luas.persegi import *
from luas.persegipanjang import *
from luas.segitiga import *
from luas.jajargenjang import *
from luas.trapesium import *
from volume.kubus import *
from volume.balok import *
from volume.kerucut import *
from volume.tabung import *
from volume.limas import *
from volume.prisma import *



def main():
    choice = int(input("Pilihan Bangun\n1. 2 Dimensi\n2. 3 Dimensi\nMasukkan bangun:"))
    if choice == 1:
        print("Pilihan Bangun\n1. Persegi\n2. Persegi Panjang\n3. Segitiga\n4. Lingkaran\n5. Jajar Genjang\n6. Trapesium")
        twoD = int(input("Masukkan bangun 2D 1 - 6:"))
        if twoD == 1:
            luasPersegi()
        elif twoD == 2:
            luasPersegiPanjang()
        elif twoD == 3:
            luasSegitiga()
        elif twoD == 4:
            luasLingkaran()
        elif twoD == 5:
            luasJajargenjang()
        elif twoD == 6:
            luasTrapesium()
        else:
            print("OOPSS, Pilihan kamu invalid. ")
            pil = input("Coba lagi? y/n").lower
            if pil=="y":
                main()
            else:
                exit()
    elif choice == 2:
        print("Pilihan Bangun\n1. Persegi\n2. Persegi Panjang\n3. Segitiga\n4. Lingkaran\n5. Jajar Genjang\n6. Trapesium")
        twoD = int(input("Masukkan bangun 3D 1 - 6:"))
        if twoD == 1:
            volumeKubus()
        elif twoD == 2:
            volumeBalok()
        elif twoD == 3:
            volumeTabung()
        elif twoD == 4:
            volumeKerucut()
        elif twoD == 5:
            volumeLimas()
        elif twoD == 6:
            volumePrisma()
        else:
            print("OOPSS, Pilihan kamu invalid. ")
            pil = input("Coba lagi? y/n").lower
            if pil=="y":
                main()
            else:
                exit()
    else:
        print("OOPSS, Pilihan kamu invalid. ")
        pil = input("Coba lagi? y/n").lower
        if pil=="y":
            main()
        else:
            exit()

main()

