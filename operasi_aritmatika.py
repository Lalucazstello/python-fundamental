a = 10
b = 3

# penjumlahan
hasil = a + b
print(a,"+",b,"=",hasil)

# PENGURANGAN
hasil = a - b
print(a,"-",b,"=",hasil)

# perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# pembagian
hasil = a / b
print(a,"/",b,"=",hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# operasi modulus %
hasil = a % b
print(a,"%",b,"=",hasil)

# floor division(kebalikan modulus)
hasil = a // b
print(a,"//",b,"=",hasil)

# prioritas operasi, operational precedence
'''
1. ()
2. exponen **
3. perkalian dan teman" * / ** % //
4. pertambahan dan pengurangan + -
'''
x =  3
y = 2 
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)


hasil = x + y * z
print(x,'+','y','*',z,'=',hasil)

# kurung akan mengambil langkah paling pertamas
hasil = (x + y) * z
print('(',x,'+','y',') *',z,'=',hasil)

