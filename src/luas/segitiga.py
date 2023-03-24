def luasSegitiga():
    # Minta input dari pengguna untuk ukuran alas segitiga
    a = float(input("Masukkan ukuran alas dalam centimeter:"))
    # Minta input dari pengguna untuk ukuran tinggi segitiga
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))
    # Hitung luas segitiga dengan rumus 0.5 * alas * tinggi
    luas = 0.5 * a * t
    # Tampilkan hasil luas segitiga ke layar
    print(f"Luas bangun segitiga tersebut adalah {luas} cm\u00B2")
