
# slicing in for loop  


offices=['lohitr',12345,'sei','daiki',90989,'python','KLE']


for  office in offices[0:3]:
    print(office) 


# check the item is matching

for office in offices:
    
    if office=='python':
        print('the programming language is',office)

    elif office=='KLsE':
        print('the university is', office)
        
    else:
        print('all other is', office)
        
        
        # one more example on for 
        
print('-----------------------------------------------')

# slicing in the loop 

offices=['japan','Amarica','Brazil','Newyork','india']

for off in offices[0:3]:
    print(off)
print('------------------')

# check the item is matching or not 

for off in offices:
    if off=='india':
        print('India and Japan')
    
    elif off =='Amarica':
        print('America and North Korea')
    
    else:
        print('Brazil')