# sets 

# no dublicate/repeated values 

# create an output set which contains only the even numbers that are present in the input list.


input_list=[1,2,4,1,4,6,6,8,2,99,1,5,3,6,8]

output_set=set()

for var in input_list:
    if var %2==0:
        output_set.add(var)

print(' output set', output_set)



# comprehension 
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] 

set_using_comp = {var for var in input_list if var % 2 == 0} 

print("Output Set using set comprehensions:", 
							set_using_comp) 



# list => [] 
# tuple =>()
# dict =>{}
# set ={}