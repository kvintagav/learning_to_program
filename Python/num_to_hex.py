
import struct 
import os

def reverse_string(string):
	string_out =""
	for i in range(len(string)-1,-1,-1):
		string_out+=string[i]
	return string_out

def print_hex(number):
	num = number
	string = ""
	if num>0: 
		while num>=1:
			ost = num%16
			if ost<10:
				string+=str(int(ost))
			elif ost==10:
				string+="A"
			elif ost==11:
				string+="B"
			elif ost==12:
				string+="C"
			elif ost==13:
				string+="D"
			elif ost==14:
				string+="E"
			elif ost==15:
				string+="F"
			else:
				print("Error")
				break
			num = int(num/16)
		print (reverse_string(string))
		return True	
	else:
		return False	


num = 1234567890
print_hex(num)
print (hex(num))

numb =hex(num)
print (numb)
