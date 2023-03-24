import math #mengimport module math

def volumeKerucut():
    # meminta user untuk memasukkan ukuran jari-jari alas dan tinggi kerucut dalam cm
    r = float(input("Masukkan ukuran jari-jari alas dalam centimeter:"))
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))
    # menghitung volume kerucut dengan menggunakan rumus 1/3 * (pi * r * r) * t
    volume = 1/3 * (math.pi * r * r) * t
    # mencetak hasil volume kerucut 
    print(f"Volume bangun ruang tersebut adalah {volume} cm\u00B3")

