lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for x in range(lower,upper + 1):
   # prime numbers are greater than 1
   if x > 1:
       for i in range(2,num):
           if (x % i) == 0:
               break
       else:
           print(x)
