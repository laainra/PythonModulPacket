
def volumeLimas():
    segi = int(input("Masukkan jumlah segi  antara 3-6:"))  # meminta input dari pengguna untuk jumlah sisi
    tinggi = float(input("Masukkan ukuruan tinggi dalam centimeter:")) # meminta input dari pengguna untuk tinggi limas
    
    # melakukan pengecekan kondisi jumlah segi dengan menggunakan if, elif, dan else
    if segi == 3: # jika jumlah segi 3 makaa akan dijalankan blok kode berikut 
        alas = float(input("Masukkan luas segitiga alas dalam satuan cm\u00B2: ")) # meminta inputan untuk ukuran alas
        volume = 1/3 * alas * tinggi  # menghitung volume
        print(f"Volume limas segitiga adalah {volume} cm\u00B3")# menampilkan volume
    elif segi == 4: # jika jumlah segi 4 makaa akan dijalankan blok kode berikut 
        alas = float(input("Masukkan luas segiempat alas dalam satuan cm\u00B2: "))
        volume = 1/3 * alas * tinggi  # menghitung volume
        print(f"Volume limas segiempat adalah {volume} cm\u00B3")# menampilkan volume
    elif segi == 5: # jika jumlah segi 5 makaa akan dijalankan blok kode berikut 
        alas = float(input("Masukkan luas segi lima alas dalam satuan cm\u00B2: "))
        volume = 1/3 * alas * tinggi  # menghitung volume
        print(f"Volume limas segi lima adalah {volume} cm\u00B3") # menampilkan volume
    elif segi == 6:# jika jumlah segi 6 makaa akan dijalankan blok kode berikut 
        alas = float(input("Masukkan luas segi enam alas dalam satuan cm\u00B2: "))
        volume = 1/3 * alas * tinggi  # menghitung volume
        print(f"Volume limas segi enam adalah {volume} cm\u00B3") # menampilkan volume
    else:
        print("OOOPS, segi yang dimasukkan tidak valid. coba lagi.") # mencetak pesan error jika jumlah sisi yang dimasukkan tidak valid.


volumeLimas()