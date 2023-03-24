def luasTrapesium():
    # meminta input ukuran sisi atas, sisi bawah, dan tinggi dari pengguna
    a = float(input("Masukkan ukuran sisi atas centimeter:"))
    b = float(input("Masukkan ukuran sisi bawah centimeter:"))
    t = float(input("Masukkan ukuran tinggi dalam centimeter:"))
    # menghitung luas trapesium dengan rumus (a+b)/2 * t
    luas = 0.5 * (a + b) * t
    # mencetak hasil perhitungan ke layar
    print(f"Luas bangun trapesium tersebut adalah {luas} cm\u00B2")
