def volumeLimas():
    segi = int(input("Masukkan jumlah segi  antara 3-6:"))
    tinggi = float(input("Masukkan ukuruan tinggi dalam centimeter:"))
    if segi == 3:
        alas = float(input("Masukkan luas segitiga alas dalam satuan cm\u00B2: "))
        volume = 1/3 * alas * tinggi
        print(f"Volume limas segitiga adalah {volume} cm\u00B3")
    elif segi == 4:
        alas = float(input("Masukkan luas segiempat alas dalam satuan cm\u00B2: "))
        volume = 1/3 * alas * tinggi
        print(f"Volume limas segiempat adalah {volume} cm\u00B3")
    elif segi == 5:
        alas = float(input("Masukkan luas segi lima alas dalam satuan cm\u00B2: "))
        volume = 1/3 * alas * tinggi
        print(f"Volume limas segi lima adalah {volume} cm\u00B3")
    elif segi == 6:
        alas = float(input("Masukkan luas segi enam alas dalam satuan cm\u00B2: "))
        volume = 1/3 * alas * tinggi
        print(f"Volume limas segi enam adalah {volume} cm\u00B3")
    else:
        print("OOOPS, segi yang dimasukkan tidak valid. coba lagi.")
