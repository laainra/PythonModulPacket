# membuat fungsi untuk menghitung luas persegi
def luasPersegi():
    # meminta inputan dari user untuk ukuran sisi persegi
    s = float(input("Masukkan ukuran sisi dalam centimeter:"))
    # menghitung luas persegi dengan rumus sisi x sisi
    luas = s * s
    # menampilkan hasil perhitungan ke layar dengan menggunakan f-string
    print(f"Luas bangun persegi tersebut adalah {luas} cm\u00B2")
