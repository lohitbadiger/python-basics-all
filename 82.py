# list comprehensions 

# Normal way 
numbers=[1,2,3,4,5,6] 
double =[]


for number in numbers:
    double.append(number*2)
print(double)


print('==-------------------------')


double.append(number*2 for number in numbers)
print('this number would be', double[:-1])

