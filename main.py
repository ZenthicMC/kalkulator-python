#
# Code sama sekali tidak optimal & bertele-tele
# Maklum adaptasi dari java & sekalian eksperimen syntax python
#

import os

os.system('cls')
print("===================================")
print("\n Applikasi Kalkulator Sederhana\n")
print("===================================")

bil1 = float(input("Masukkan Bilangan Pertama: "))
bil2 = float(input("Masukkan Bilangan Kedua: "))

print("\n\n===================================")
print("Pilih Operasi Perhitungan:\n")
print(" 1. Penjumlahan (+)")
print(" 2. Pengurangan (-)")
print(" 3. Perkalian (*)")
print(" 4. Pembagian (/)")
print("===================================")
pilOperasi = input("Pilihan (1/2/3/4) > ")

if pilOperasi=="1":
    hasil = bil1 + bil2
elif pilOperasi=="2":
    hasil = bil1 - bil2
elif pilOperasi=="3":
    hasil = bil1 * bil2
elif pilOperasi=="4":
    hasil = bil1 / bil2

print("===================================")
print("Hasil Perhitungan: \n")
print(" Bilangan 1: " + str(bil1))
print(" Bilangan 2: " + str(bil2))
print("\n JAWABAN = " + str(hasil))
print("===================================")
 
