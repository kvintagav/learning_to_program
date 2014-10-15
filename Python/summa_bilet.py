"""Написать программу определения количества шестизначных 'счастливых' билетов, 
у которых сумма первых 3 десятичных цифр равна сумме 3 последних десятичных цифр."""


def summa():
	lis=[0,1,2,3,4,5,6,7,8,9]
	rez=0
	for a1 in lis:
		for a2 in lis:
			for a3 in lis:
				for a4 in lis:
					for a5 in lis:
						a6=a1+a2+a3-(a4+a5)
						if a6>=0 and a6<=9:
							rez+=1
						
		
					 
	return rez 


def summa2():
	lis=[0,1,2,3,4,5,6,7,8,9]
	rez=0
	for a1 in lis:
		for a2 in lis:
			for a3 in lis:
				for a4 in lis:
					for a5 in lis:
						for a6 in lis:
							if a1+a2+a3==a4+a5+a6:
								rez+=1
						
		
					 
	return rez 

print (summa())
