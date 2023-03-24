def luasTrapesium():
    a = float(input("Masukkan ukuran sisi atas centimeter:"))
    b = float(input("Masukkan ukuran sisi bawah centimeter:"))
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))
    luas = 0.5 * (a + b) * t
    print(f"Luas bangun trapesium tersebut adalah {luas} cm\u00B2")
