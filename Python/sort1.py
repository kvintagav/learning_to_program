import sys

n = int(input())
#lineIn= list(map(int, input().split()))
input = sys.stdin.read()
lineIn = input.split()

cached=[]
for curr in range (0,11):
	cached.append(0)

for index in range (0,n):
    cached[int(lineIn[index])]+=1

k=0	
lineOut=[]
for index in range (0,11):
	for j in range (0,cached[index]):
		lineOut.append(index)
		
		
sys.stdout.write(str(lineOut))

