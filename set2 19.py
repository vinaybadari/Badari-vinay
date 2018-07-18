def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)
f=int(input( ))
print(factorial(f))
