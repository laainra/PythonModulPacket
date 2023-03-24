# mengimport modul math
import math

# membuat fungsi untuk menghitung luas lingkaran
def luasLingkaran():
    # meminta inputan dari user untuk ukuran jari-jari lingkaran
    r = float(input("Masukkan ukuran jari-jari dalam centimeter:"))
    # menghitung luas lingkaran dengan menggunakan rumus pi x r^2 dari modul math
    luas = math.pi * r * r
    # menampilkan hasil perhitungan ke layar dengan menggunakan f-string
    print(f"Luas bangun lingkaran tersebut adalah {luas} cm\u00B2")
