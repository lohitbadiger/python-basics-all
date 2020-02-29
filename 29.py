# I WANT print factorial of an number 


number=int(input('enter the number to find factorial of number '))

fac=1

for i in range(1,number+1):
    
    fac=fac*i
print('factorial of this number', number, 'is', fac)
