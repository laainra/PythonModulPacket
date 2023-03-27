# Mengimport seluruh module yang ada pada direktori luas dan volume
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


#mendeklarasikan function main() atau fungsi utama
def main():
    confirm = "y"
    while confirm=="y":
        choice = int(input("Pilihan Bangun\n1. 2 Dimensi\n2. 3 Dimensi\nMasukkan bangun:")) # meminta input pilihan dimensi bangun
        if choice == 1: # jika pilihan bangun 2D
            print("Pilihan Bangun\n1. Persegi\n2. Persegi Panjang\n3. Segitiga\n4. Lingkaran\n5. Jajar Genjang\n6. Trapesium") # menampilkan pilihan bangun 2D
            twoD = int(input("Masukkan bangun 2D 1 - 6:")) # meminta input pilihan bangun 2D
            if twoD == 1:  # jika memilih bangun persegi
                luasPersegi()  #memanggil function perhitungan bangun
            elif twoD == 2: # jika memilih bangun persegi panjang
                luasPersegiPanjang() #memanggil function perhitungan bangun
            elif twoD == 3: # jika memilih bangun segitiga
                luasSegitiga() #memanggil function perhitungan bangun
            elif twoD == 4: # jika memilih bangun lingkaran
                luasLingkaran() #memanggil function perhitungan bangun
            elif twoD == 5: # jika memilih bangun jajar genjang
                luasJajargenjang() #memanggil function perhitungan bangun
            elif twoD == 6: # jika memilih bangun trapesium
                luasTrapesium() #memanggil function perhitungan bangun
            else:
                print("OOPSS, Pilihan kamu invalid. ") # jika memilih pilihan yang tidak valid
                pil = input("Coba lagi? y/n").lower() # input untuk mengulang atau tidak
                if pil=="y":
                    main()# jika memilih untuk mengulang, jalankan fungsi main()
                else:
                    exit() # jika tidak, keluar dari program
        elif choice == 2: # jika memilih bangun 3D
            print("Pilihan Bangun\n1. Kubus\n2. Balok\n3. Tabung\n4. Kerucut\n5. Limas\n6. Prisma") # menampilkan pilihan bangun 3D
            twoD = int(input("Masukkan bangun 3D 1 - 6:")) # meminta input pilihan bangun 3D
            if twoD == 1: # jika memilih bangun kubus
                volumeKubus() #memanggil function perhitungan bangun
            elif twoD == 2: # jika memilih bangun balok
                volumeBalok() #memanggil function perhitungan bangun
            elif twoD == 3: # jika memilih bangun tabung
                volumeTabung() #memanggil function perhitungan bangun
            elif twoD == 4: # jika memilih bangun kerucut
                volumeKerucut() #memanggil function perhitungan bangun
            elif twoD == 5: # jika memilih bangun limas
                volumeLimas() #memanggil function perhitungan bangun
            elif twoD == 6: # jika memilih bangun prisma
                volumePrisma() #memanggil function perhitungan bangun
            else:
                print("OOPSS, Pilihan kamu invalid. ") # jika memilih pilihan yang tidak valid
                pil = input("Coba lagi? y/n").lower() # input untuk mengulang atau tidak
                if pil=="y":
                    main() # jika memilih untuk mengulang, jalankan fungsi main()
                else:
                    exit() # jika tidak, keluar dari program
        else:
            print("OOPSS, Pilihan kamu invalid. ") # jika memilih pilihan yang tidak valid
        confirm = input("Coba lagi? y/n:").lower() # input untuk mengulang atau tidak
        if confirm=="y":
            main() # jika memilih untuk mengulang, jalankan fungsi main()
        else:
            exit() # jika tidak, keluar dari program
    

main() # menjalankan function main()

