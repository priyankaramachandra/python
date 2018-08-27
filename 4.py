# finding the vowles in the given in put

vol = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
s = input("Enter a phrase: ")
c= 0
for i in s:
    if i in vol:
        c = 1+c
print(c)