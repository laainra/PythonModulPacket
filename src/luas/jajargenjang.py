# membuat fungsi untuk menghitung luas jajar genjang
def luasJajargenjang():
    # meminta inputan dari user untuk ukuran alas dan tinggi
    a = float(input("Masukkan ukuran alas dalam centimeter:"))
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))
    # menghitung luas jajar genjang dengan rumus alas x tinggi
    luas = a * t
    # menampilkan hasil perhitungan ke layar dengan menggunakan f-string
    print(f"Luas bangun jajar genjang tersebut adalah {luas} cm\u00B2")
