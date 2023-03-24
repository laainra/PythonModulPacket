def volumeKubus():
    # Mengambil input dari pengguna berupa panjang sisi kubus dalam satuan cm.
    s = float(input("Masukkan ukuran sisi dalam centimeter:"))
    # Menghitung volume kubus dengan memangkatkan sisi dengan 3
    vol = s**3
    # Mencetak hasil volume kubus yang sudah dihitung dengan format string.
    print(f"Luas bangun persegi tersebut adalah {vol} cm\u00B3")
