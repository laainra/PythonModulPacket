import math
    
def volumePrisma():
    segi = int(input("Masukkan jumlah sisi segi prisma(3-10): "))
    tinggi = float(input("Masukkan tinggi prisma dalam satuan cm: "))

    if segi == 3: # segitiga
        alas = float(input("Masukkan luas alas segitiga dalam satuan cm\u00B2: "))
        volume = 1/2 * alas * tinggi
        print(f"Volume prisma segitiga adalah {volume} cm\u00B3")
    elif segi == 4: # segiempat
        panjang = float(input("Masukkan panjang alas segiempat dalam satuan cm: "))
        lebar = float(input("Masukkan lebar alas segiempat dalam satuan cm: "))
        volume = panjang * lebar * tinggi
        print(f"Volume prisma segiempat adalah {volume} cm\u00B3")
    elif segi == 5: # segilima
        a = float(input("Masukkan panjang sisi segilima dalam satuan cm: "))
        b = float(input("Masukkan lebar sisi segilima dalam satuan cm: "))
        volume = 5/2 * a * b * tinggi
        print(f"Volume prisma segilima adalah {volume} cm\u00B3")
    elif segi == 6: # segienam
        s = float(input("Masukkan panjang sisi segienam dalam satuan cm: "))
        volume = 3/2 * math.sqrt(3) * s**2 * tinggi
        print(f"Volume prisma segienam adalah {volume} cm\u00B3")
    elif segi == 8: # segilapan
        a = float(input("Masukkan panjang sisi segilapan dalam satuan cm: "))
        volume = 2 * (1 + math.sqrt(2)) * a**2 * tinggi
        print(f"Volume prisma segilapan adalah {volume} cm\u00B3")
    elif segi == 10: # segibelas
        a = float(input("Masukkan panjang sisi segibelas dalam satuan cm: "))
        volume = 5/2 * (1 + math.sqrt(5)) * a**2 * tinggi
        print(f"Volume prisma segibelas adalah {volume} cm\u00B3")
    else:
        print("OOPSSS... Segi-n tidak valid. Coba lagi.")
