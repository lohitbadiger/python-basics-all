all_number=[]
number=int(input('How many numbers are there in all_number')) 

for n in range(number):
    numbers=int(input('enter values of these numbers'))
    all_number.append(numbers)
    
print('total sum of all the items in the list', sum(all_number)/number)