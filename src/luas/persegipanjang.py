# membuat fungsi untuk menghitung luas persegi panjang
def luasPersegiPanjang():
    # meminta inputan dari user untuk ukuran panjang dan lebar persegi panjang
    p = float(input("Masukkan ukuran panjang dalam centimeter:"))
    l = float(input("Masukkan ukuran lebar dalam centimeter:"))
    # menghitung luas persegi panjang dengan rumus panjang x lebar
    luas = p * l
    # menampilkan hasil perhitungan ke layar dengan menggunakan f-string
    print(f"Luas bangun persegi panjang tersebut adalah {luas} cm\u00B2")
