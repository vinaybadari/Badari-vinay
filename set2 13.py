n = int(input())
for i in range(2, int(n/2)):
    if n % i  == 0:
        print("no")
        break
else:
    print("yes")
