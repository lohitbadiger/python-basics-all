# python program showing how to have multiple inputs using split 


# taking all input at once 

# x,y=input('Enter the values for x and y :').split()

# print('Value for x :',x)
# print('Value for y:',y)


# a,b,c=input('Enter value for abc: ').split()
# print(a,b,c)


a,b=input('Enter the value for a,b :').split()
print(f'the value of a {a} and value for b is {b}')

print('the value of a {0} and value for b is {1}'.format(a,b))








a=input('Enter a')

b=input('Enter b')

a=float(a)
b=float(b)

print(f'{a:.3f}')
print(f'{b:.4f}')
