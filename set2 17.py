y=int(input())
t=y
num=0
while y!=0:
	v=y%10
	y=y//10
	num += v**3
if num==t:
	print("yes")
else:
	print("no")
