import math

def volumeTabung():
    r = float(input("Masukkan ukuran jari-jari alas dalam centimeter:"))
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))
    volume = (math.pi * r * r) * t
    print(f"Volume bangun ruang tersebut adalah {volume} cm\u00B3")


