import sys

#input_num = sys.stdin.read().split()
#number = int(input_num[0])

a=input()
number=int(a)%60
print (number)
prev_n=1
next_n=1
rez=next_n
i=2
while i<number:
    rez=(prev_n+next_n)%10
    prev_n=next_n
    next_n=rez
    i+=1
    print (i,rez)
	
print (rez)    
        