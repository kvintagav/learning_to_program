friends = ['andrey','tanya','ira']
for friend in friends:
	print ('Happay',friend)
print ('Done')
import random


def mini(values):
	smallest = None
	for value in values:
		if smallest is None or value<smallest:
			smallest=value
	return smallest

count = 0
total = 0 
largest = 0
for iterval in range(10):
	count = count + 1
	total += iterval

	value = random.randint(0,100)
	if largest is None or value>largest:
		largest = value
	print ('Value:',value,'Largest:',largest)
	
print ('Count:',count,' Total:',total)

list_number=[]

for num in range(10):
	list_number.append(random.randint(0,100))

print (list_number)
minimum=mini(list_number)
print ('minimum:',minimum)