x,y=input().split()
x=int(x)
y=int(y)
for a in range(x,y):
	t=a
	n=0
	while a!=0:
		b=a%10
		a=a//10
		n += b**3
	if n==t:
		print(t,end=" ")
