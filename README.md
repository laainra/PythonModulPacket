Program Menghitung Luas Bangun 2 Dimensi dan Volume Bangun 3 Dimensi

Program ini menggunakan konsep modul dan paket untuk menghitung luas bangun 2 dimensi dan volume bangun 3 dimensi. Modul-modul yang digunakan antara lain:

    bangun_dua_dimensi.py : Modul ini berisi fungsi-fungsi untuk menghitung luas bangun 2 dimensi, seperti lingkaran, segitiga, dan persegi panjang.
    bangun_tiga_dimensi.py : Modul ini berisi fungsi-fungsi untuk menghitung volume bangun 3 dimensi, seperti kubus, balok, dan tabung.
    __init__.py : Modul ini berfungsi sebagai penghubung antara modul-modul di atas dan menjadi paket.

Penggunaan

Untuk menggunakan program ini, Anda perlu mengimport modul yang sesuai dengan bangun yang ingin dihitung luas atau volumenya.

Contoh penggunaan untuk menghitung luas lingkaran:

python

from bangun_dua_dimensi import lingkaran

jari_jari = 7
luas = lingkaran.luas(jari_jari)

print("Luas lingkaran dengan jari-jari {} adalah {}".format(jari_jari, luas))

Contoh penggunaan untuk menghitung volume kubus:

python

from bangun_tiga_dimensi import kubus

sisi = 5
volume = kubus.volume(sisi)

print("Volume kubus dengan sisi {} adalah {}".format(sisi, volume))
