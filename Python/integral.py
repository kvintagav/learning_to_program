"""вычисление интеграла методом трапеций и методом симпсона """
import math

first = lambda x:1.0/x

second = lambda x: math.exp(-x**2)

third = lambda x:math.sin(x)/x

firth = lambda x:x/(math.exp(x)+1)

fifty =lambda x: 1/(x*math.sqrt(x))

def integral_trapetion(left=0,right=1,mount_part = 2,our_func=first):
	rezult= 0.0
	value = (our_func(left)+our_func(right))/2
	for index in range(1,mount_part):
		value+= our_func(left+(right-left)*(index/mount_part))
	rezult = value*(right-left)/mount_part
	return rezult
	

def integral_simpson(left=0,right=1,mount_part = 2,our_func=first):
	rezult= 0.0
	value = (our_func(left)+our_func(right))

	for index in range(1,mount_part):
		value+= 2*our_func(left+(right-left)*(index/mount_part))
	for index in range(0,mount_part):
		value+= 4*our_func(left+(right-left)*(index/mount_part)+(right-left)/(2*mount_part))
	rezult = value*(right-left)/(mount_part*2*3)
	return rezult

	

print ("1/x - simpson",integral_simpson(1,3,4,first))
print ("1/x - trapetion",integral_trapetion(1,3,4,first))

print ("exp(-x^2) - simpson",integral_simpson(0,2,8,second))
print ("exp(-x^2) - trapetion",integral_trapetion(0,2,8,second))

print ("sin(x)/x - simpson",integral_simpson(0.00001,3.14,4,third))
print ("sin(x)/x - trapetion",integral_trapetion(0.00001,3.14,4,third))

print ("x/(e^x+1) - simpson  ",integral_simpson(0,3,4,firth))
print ("x/(e^x+1) - trapetion",integral_simpson(0,3,60,firth))

def summa_trapetion(left=0,right=1,our_func=first):
	value = 0.0

	value+=our_func(left)/2 +our_func(right)/2

	value+=integral_trapetion(left=left,right=right,mount_part = (right-left),our_func=our_func)

	return value


print (summa_trapetion(1,20,fifty))
