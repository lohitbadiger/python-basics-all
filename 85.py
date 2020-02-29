# inbuilt  modules 




countries=['India','USA', 'China']
countries2=['Japan','Canada','North Korea']


output={}

# using the for loop 

for(key,value) in zip(countries,countries2):
    output[key]=value
print(output)


# comprehension 


