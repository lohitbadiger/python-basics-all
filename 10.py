# list

# list values can be changed later , we call them as  mutable 


# i can store different types of data type

# ()=>tuple 
# []=>list 

words=[1,2,3,4,5,6,'lohit','yuri',True,12.34,('lohit','john')]

print('my list is',words)

print(words[2])
print(words[2:])

print(words[2:5])

print(words[6][3])

print('-------------------------')
print('lohit' in words)

print('-------------------------')
words[6]='daiki and sei'

print(words)

print('-------------------------')
print(words[10][0])

print('-'*20)

# in operator
print(1 in words)


words=[1,2,3,4,5,6,'lohit','yuri',True,12.34,('lohit','john')]


print(('lohit','john') in words)

# append function in list 

# it adds the new element at last 

create=['maths','science']
create.append('python')

print(create)

# insert(): Inserts an elements at specified position.

one_more=['maths','algebra','php']

one_more.insert(1,'python')
print(one_more)


# extend in list 
# extend(): Adds contents to name2 to the end of name.

name=['lohit','jogn','daiki', 'sei']
name2=[1,2,3,4,5,6,7]

name2.extend(name)
print(name2)

print('--------------------------------------------------')

# REMOVE


create.remove('maths')
print(create)

print('--------------------------------------------------')

# REMOVE THE ELEMETNS FROM INDEX
create.pop(0)
print(create)


print('--------------------------------------------------')
name=['hello','good','morning','yuki','yuki']
count=name.count('yuki')
print(count)

print('----------------------------------------')

# find the index of the yuki 
name=['hello','yuki','good','morning','yuki',]
count=name.index('yuki')
print(count)


random = ['a', ('a', 'b'), [3, 4]]
# index of ('a', 'b')
index = random.index(('a', 'b'))
print("The index of ('a', 'b'):", index)
# index of [3, 4]
index = random.index([3, 4])
print("The index of [3, 4]:", index)
