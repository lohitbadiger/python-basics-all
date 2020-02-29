# sets 
# union in python
 
 
set1={1,2,5,3,4,5}
set2={23,45,1,24,6,7,3,4}

print('Union', set1 |set2)

####################################

print('common items are called intersection',set1&set2)

####################################

# difference 
# so from set1=>{2,5} from set2=>{23,45,24,6,7}
# its like how many not matching item left in the sets

print("Difference :",set1 -set2)



# symmetric difference 
a={1,2,3,4,5,6}
b={4,5,6,7,8}

# symmetric differnce is opposite of intersection

print("Symmetric difference :", a ^ b) 