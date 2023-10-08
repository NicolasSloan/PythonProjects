Intvar= 69
print(Intvar)
strvar= 'hello!'
print(strvar)
floatvar=420.69
print(floatvar)

X=120
Y=2
Z=7
print(X+Y)
print(X*Y)
print(X/Y)
print(Z%Y)

if Y>0 and Z>0:
    print('Both Y and Z are greater than 0!')
elif Y<0 or Z<0:
    print('Either Y or Z are not greater than 0!')
elif not(Y>0 and Z>0):
    print('Both Y and Z are not greater than 0!')
else:
    print('Houston we have a problem')

mylist = ['purple', 'black', 'gold']
for color in mylist:
    print(color)

A=10
while A>0:
    print(A)
    A-=1

mytuple = ('You', 'cant', 'change', 'me!')
for words in mytuple:
    print(words)


def add_two_numbers(arg1, arg2):
    return arg1+arg2

print(add_two_numbers(5, 2))
