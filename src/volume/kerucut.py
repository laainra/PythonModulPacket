import math

def volumeKerucut():
    r = float(input("Masukkan ukuran jari-jari alas dalam centimeter:"))
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))
    volume = 1/3 * (math.pi * r * r) * t
    print(f"Volume bangun ruang tersebut adalah {volume} cm\u00B3")

