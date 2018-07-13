a=str(raw_input())
b=('a','e','i','o','u')
if a.isalpha():
     if a in b:
         print("vowel")
     else:
         print("Consonant")
else:
     print("invalid")
