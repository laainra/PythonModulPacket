def volumeBalok():
    p = float(input("Masukkan ukuran panjang dalam centimeter:")) # meminta input dari user untuk panjang
    l = float(input("Masukkan ukuran lebar dalam centimeter:")) # meminta input dari user untuk lebar
    t = float(input("Masukkan ukuran tinggi dalam centimeter:")) # meminta input dari user untuk tinggi
    volume = p * l * t # menghitung volume dengan rumus p * l * t
    print(f"Volume bangun ruang tersebut adalah {volume} cm\u00B3") # menampilkan hasil volume dengan format string
