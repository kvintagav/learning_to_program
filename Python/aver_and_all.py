"""
Вычисление среднего суммы и количества
"""
import random

def random_list(length):
	""" full random list with length length"""
	numbers = []
	for num in range(length):
		numbers.append(random.randint(0,100))
	return numbers	

def average(values):
	average = 0.0
	for value in values:
		average+=value
		
	return (average/len(values))

def summa(values):
	summa = 0
	for value in values:
		summa+=value
	return summa

numbers = []
while True:
	line=input("Enter a number: ")
	if line =='done':
		break
	try:
		number=int(line)
		numbers.append(number)
		print(number)
	except ValueError:
		print ('bad number')

if len(numbers) ==0:
	print('Not numbers')
else:
	print (average(numbers),summa(numbers),len(numbers))
