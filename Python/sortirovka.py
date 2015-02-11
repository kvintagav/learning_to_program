import  random 

def sort_vstavka(size=10):
	""" алгоритм сортировки методом вставки
	Эффективен при сортировке небольшого количества элементов"""
	a=[]
	numb_operation = 0 
	for index in range(size):
		a.append(random.randint(0,size))
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
	"""алгоритм сортировки выбором"""
	a=[]
	numb_operation = 0;
	for index in range(size):
		a.append(random.randint(0,size))
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

def sort_vstavka_vs(Array,left,right):
	""" алгоритм сортировки методом вставки
	Эффективен при сортировке небольшого количества элементов"""
	
	numb_operation = 0 
	numb_operation+=(right - left);
	for index in range(left+1,right-left+1):
		numb_operation+=4
		key=Array[index]
		ind_vst=index-1
		while ind_vst>=0 and Array[ind_vst]>key:
			Array[ind_vst+1] = Array[ind_vst]
			ind_vst-=1
			numb_operation+=2
		Array[ind_vst+1]=key
	
	return (numb_operation)

def Merge(Array ,left , center , right):
	numb_operation = 0
	n1 = center - left +1
	n2 = right - center 
	Left_a = []
	Right_a = []
	for index in range(n1):
		numb_operation+=2
		Left_a.append(Array[left+index])
	for index in range(n2):
		numb_operation+=2
		Right_a.append(Array[center+index+1])
	Left_a.append(10000000000000)
	Right_a.append(10000000000000)
	#print (Left_a)
	#print (Right_a)
	i = 0
	j = 0	
	numb_operation+=11
	for k in range (left,right+1):		
		numb_operation+=1
		if Left_a[i]<=Right_a[j]:
			numb_operation+=2
			Array[k] = Left_a[i]
			i+=1
		else:
			numb_operation+=2
			Array[k] = Right_a[j]
			j+=1
	return numb_operation



def sort_slianie(Array, left ,right ):
	"""алгоритм сортировки методом слияния """
	"""добавить метод вставки для небольших размеров подмассива"""
	numb_operation=1
	if left < right:
		numb_operation+=1
		center=(left+right)//2	
		numb_operation+=sort_slianie(Array = Array,left = left,right = center)
		numb_operation+=sort_slianie(Array = Array,left = center+1,right = right)
		numb_operation+=Merge(Array = Array,left = left,center = center,right = right)
	return numb_operation

def sort_slianie_vstavka(Array, left ,right ,length_vstavka):
	"""алгоритм сортировки методом слияния c добавленным методом вставки для небольших размеров подмассива"""
	numb_operation=1
	if (right - left)>length_vstavka:
		#print("slianie")
		numb_operation+=1
		center=(left+right)//2	
		numb_operation+=sort_slianie_vstavka(Array = Array,left = left,right = center,length_vstavka = length_vstavka)
		numb_operation+=sort_slianie_vstavka(Array = Array,left = center+1,right = right,length_vstavka = length_vstavka)
		numb_operation+=Merge(Array = Array,left = left,center = center,right = right)
	else:
		#print("vstavka")
		numb_operation = sort_vstavka_vs(Array = Array,left = left,right = right)	


	return numb_operation


def sort_puzirek(Array):
	numb_operation =0 
	numb_operation+=1
	for index in range(0,len(Array)):
		
		numb_operation+=2
		for j_ind in range(len(Array)-1,index,-1):
			numb_operation+=2
			
			if Array[j_ind]<Array[j_ind-1]:
				numb_operation+=3
				mass = Array[j_ind]
				Array[j_ind]=Array[j_ind-1]
				Array[j_ind-1]=mass

	return numb_operation

def test_puzirek():
	SIZE = 100
	massiv_puz=[]
	for index in range(SIZE):
		massiv_puz.append(random.randint(0,SIZE))
	print (massiv_puz)	
	numb_operation = sort_puzirek(Array = massiv_puz)

	print (massiv_puz)
	print (numb_operation) 



def test_slianie_vstavka():

	SIZE = 10000
	massiv_init=[]
	for index in range(SIZE):
		massiv_init.append(random.randint(0,SIZE))


	for lengs in range(1,2000,40):

		massiv=[]
		for index in range(SIZE):
			massiv.append(massiv_init[index])
		#print (massiv)

		rez = sort_slianie_vstavka(massiv,left = 0 ,right = (len(massiv)-1), length_vstavka =lengs)
		print (lengs,"number operation",rez)



def test_slianie():
	SIZE = 10000
	massiv_sl=[]
	for index in range(SIZE):
		massiv_sl.append(random.randint(0,SIZE))
	#print (massiv)

	rez = sort_slianie(massiv_sl,left = 0 ,right = (len(massiv_sl)-1))


	print ("Algoritm slianiem")
	print ("number operation",rez)

#print (massiv)
def test_vstavka():
	rez=sort_vstavka(size = 1000)
	print ("vibor=",rez)


def test_vibor():
	rez=sort_vibor(size = 1000)
	print ("vibor=",rez)

