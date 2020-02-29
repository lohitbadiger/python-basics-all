# data type set 

# removes the dublicate /repeated value 
set_of_number={1,2,3,3,4,5,6,7,7,8,9,2,4}


print(set_of_number)

set={8,8,8,8,8,8,8,8}
print(set)



sets={'a','b','c','d','e'}
sets.add('f')

print('adding the letter:',sets)

# removing the item from the sets

sets.remove('f')
print(sets)

#######
# #Intersection in python(common items)
# #intersection can be used in set 


sets1={1,2,3,4,6,5,5,5,6,88}
sets2={2,44,6,54,5,43,6,3,4,88}


print(sets1.intersection(sets2))

print('------------------')
sets3={2,4,4,5,67,8,9,2,4,88}

set4=sets1.intersection(sets2,sets3)

print('new set4 will be',set4)

print('---------------------')



