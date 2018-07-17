x,y=input().split()
x=int(x)
y=int(y)
for a in range(x,y):
	temp=a
	num=0
	while a!=0:
		b=a%10
		a=a//10
		num += b**3
	if num==temp:
		print(temp,end=" ")
