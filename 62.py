'''
create a class named Gender , Use the __init__() function to assign values 
for name and age etc 
'''
# init => initialize / started


class Gender():
    
    def __init__(self, name, age,programm, health):
        self.name=name
        self.age=age
        self.programm=programm
        self.heal=health
        
variables=Gender('sei',25,'python','so-so')

print(variables.name)



class Teeth():
    
    def __init__(self, small, big, pain):
        self.small=small
        self.bigxxxxasdasd=big
        self.paining=pain

        
        
instance=Teeth('big', 'small', 'lets go to doctor')
print(instance.small)
print(instance.bigxxxxasdasd)
print(instance.paining)

