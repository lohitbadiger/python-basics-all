# tuple data types 

a=100,'lohit'
print(a)

# tuple values i cant change later/non -mutable

list=(1,2,3,4, 'lohit')

print(list)

#select by index
print(list[0])
print(list[2])
print(list[1])


# list[2]=7

empty_tuple=()
print(empty_tuple)


# creating a non-empty tuples 

tup='python', 'program'
print(tup)

# adding  2 tuples 
# concat

tuple1=(100,200,300)

tuple2=('lohit','python')

tuple3=tuple1+tuple2
print(tuple3)

# length of tuple 
tuple10=('python','php','java','rails')
print(len(tuple10))


tuples=('abcd',89489,2.4545,'jpohjhn',2498)
tinytuple=(123,'john')

print(tuples[2:])
print(tuples[0:3])
print(tuples[:])
print(tinytuple*3)
# Prints concatenated lists
print(tuples+tinytuple)

print('--------------------')

print(tuples[::-1])



# tup=('physics','maths',1090,249)
# print(tup)
# del tup
# print(tup)
print('--------------------')


# nested tuples
n_tuple=('mouse trap', [8,7,4],(1,2,4,57,7, 'yuri'))
print(n_tuple)
print('--------------------')

print(n_tuple[1])

print('--------------------')
print(n_tuple[1][1])

print('--------------------')



my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[:-5])
print('-------------------------------------------')

print(my_tuple[0:5])

print(my_tuple[0:5:1])
print(my_tuple[0:5:2])
print(my_tuple[0:5:3])

# selct reverse
print(my_tuple[0:-2])


# membership operator


my_new_tuple=('a','b','c','d','e')

# in operation 
print('a' in my_new_tuple)
print('d' in my_new_tuple)

print('sie' in my_new_tuple)

print('---------------------------')

# not-in operation 

print('sei' not in my_new_tuple )





my_new_tuple[1]='lohit'
print(my_new_tuple)

