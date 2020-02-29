# in dict 

# 3**3=>3*3*3=>27
# # {1: 1, 3: 27, 5: 125, 7: 343}


input_values=[1,2,3,4,5,6,7,8]
out={}

# using the basic way 
for var in input_values:
    if var%2!=0:
        out[var]=var**3 
    
print('output is', out)


print('-------------------')

out={var:var**3 for var in input_values if var%2!=0}
print(out)