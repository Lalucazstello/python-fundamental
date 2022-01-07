
# program konversi celcius ke saruan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float((input("Masukkan suhu dalam celcius : ")))
print("Suhu adalah",celcius,"celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah",reamur,"reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah",kelvin,"kelvin")

# latihan konversi fahrenheit ke kelvin
fahrenheit = float(input('Masukkan Suhu dalam Fahrenheit: '))
celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin)

# kelvin ke fahrenheit
kelvin = float(input('Masukkan suhu dalam kelvin: '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit:", fahrenheit)
