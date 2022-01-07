# a = 10,aadalah variabel dengan nilai 10

# tipe data: Angka satuan (integer)
data_integer = 11
print("data : ", data_integer)
print("-data bertipe : ", type(data_integer))

# tipe data : angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("-data bertipe : ", type(data_float))

# tipe data : kumpulan karakter (string)
data_string = "jon"
print("data : ", data_string)
print("-data bertipe : ", type(data_string))

# tipe data : binner true/false (boolean)
data_boolean = True
print("data : ", data_boolean)
print("-data bertipe : ", type(data_boolean))

# tipe data khusus
# bilangan kompleks

data_kompleks = complex(5,6)
print("data : ", data_kompleks)
print("-data bertipe : ", type(data_kompleks))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("-bertipe : ",type(data_c_double))