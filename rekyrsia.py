"""Вычислить значение суммы

S = 1/1! + 1/2! + ... + 1/k!
"""



number = int(input())

print (number)

i = 2
rezult = 1.0
summa = 1.0 
while (i<=number):
	summa =summa/i 
	rezult += summa
	i+=1
	print (summa , rezult)

print (rezult)
