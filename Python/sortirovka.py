
"""скорость роста алгоритмов """

"""
i = 1

alg1 = 1
alg2 = 2
for i in range(20):
	alg1=100*i*i
	alg2=2**i
	print (i," ",alg1," ",alg2)


print (" ")
"""


""" алгоритм сортировки методом вставки
Эффективен при сортировке небольшого количества элементов"""



import  random 

def sort_vstavka(size=10):
	a=[]
	numb_operation = 0 
	for index in range(size):
		a.append(random.randint(0,size*10))
#	for index in range(size):
#		a.append(index)
	numb_operation+=size;
	for index in range(1,len(a)):
		numb_operation+=4
		key=a[index]
		ind_vst=index-1
		while ind_vst>=0 and a[ind_vst]<key:
			a[ind_vst+1] = a[ind_vst]
			ind_vst-=1
			numb_operation+=2
		a[ind_vst+1]=key
	
	return (numb_operation)

def sort_vibor(size=10):
	a=[]
	numb_operation = 0;
	for index in range(size):
		a.append(random.randint(0,size*10))
	#print(a)
	mini = 0
	for index in range(0,len(a)):
		
		mini_index=index
		numb_operation+=5
		for ind_min in range(index,len(a)):
			numb_operation+=1
			if a[ind_min]<a[mini_index]:
				numb_operation+=1
				mini_index=ind_min

		#print (index , mini)
		mini=a[mini_index]		
		a[mini_index] = a[index]
		a[index] = mini
		
	#print(a)
	return (numb_operation)

rez=sort_vibor(size = 1000)
print ("vibor=",rez)
rez=sort_vstavka(size = 1000)
print ("vstavka=",rez)
"""
rezult = []
for index in range(1,2):
	size_array = 1000
	#rez=sort_vstavka(size = size_array)
	rez=sort_vibor(size = size_array)
	rezult.append(rez)

	print ("size_array =",size_array,"numb_operation = ",rez)

print (rezult)
"""

