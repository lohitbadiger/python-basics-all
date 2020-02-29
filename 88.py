#  Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous/unknown function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:


x=lambda a:10+a


print(x(2))

# equation 
# y=20+b 

y=lambda b:20+b
print(y(10))


# equation=Y**X 

x=int(input('enter '))
y=int(input('enter '))

total=y**x
print(total)

# lambda way 

equ=lambda x, y:y**x
print(equ(2,3))


# equ=x+y+z



def myfun(n):
    return lambda a:a*n

double=myfun(3)
print(double(11))