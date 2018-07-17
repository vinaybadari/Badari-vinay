x,v=input().split()
x=int(x)
v=int(v)
for z in range(x+1,v):
	count=0
	for i in range(1,z+1):
		if z%i==0:
			count=count+1
	if count==2:
		print (z,end=" ")
