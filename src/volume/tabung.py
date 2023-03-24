import math #Mengimport module math, 

def volumeTabung():
    r = float(input("Masukkan ukuran jari-jari alas dalam centimeter:")) #  meminta input jari jari
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))   #  meminta input tinggi
    volume = (math.pi * r * r) * t # menghitung volume
    print(f"Volume bangun ruang tersebut adalah {volume} cm\u00B3") # menampilkan volume


