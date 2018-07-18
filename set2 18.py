m,y=input().split()
m=int(m)
y=int(y)
for a in range(m,y):
	t=a
	num=0
	while a!=0:
		b=a%10
		a=a//10
		num += b**3
	if num==t:
		print(t,end=" ")
