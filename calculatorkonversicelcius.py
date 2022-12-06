print("PROGRAM KONVERSI TEMPERATUR")
#kumpulan data
b = 4/5
c = (9/5)
a = float(input("masukkan data SUHU dalam celcius:"))
print("SUHU ADALAH", a)

#reamur
hasilreamur = a * b
print("CELCIUS DALAM REAMUR ADALAH:", hasilreamur)

#fahrenheit
hasilfahrenheit = a * c + 32
print("CELCIUS DALAM FAHRENHEIT:", hasilfahrenheit)

#kelvin
d = 273
hasilkelvin = a + d
print("CELCIUS DALAM KELVIN",hasilkelvin )