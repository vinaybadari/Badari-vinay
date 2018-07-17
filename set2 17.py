x=int(input())
t=x
num=0
while x!=0:
	y=x%10
	x=x//10
	num += y**3
if num==t:
	print("yes")
else:
	print("no")
