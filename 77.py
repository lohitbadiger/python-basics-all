class Future:
    fun='very nice day'
    # creating a classs level object 
    
    def __init__(self,name,age,game,system):
        self.name=name 
        self.age=age 
        self.game=game 
        self.system=system 
    
    def orbit(self):
        return f'{self.name} is -->{self.age}'
    
instance=Future('lohit',20,'baseball','linear-system')

print(f'Name is : {instance.name}')
print(f'Name is : {instance.age}')
print(f'Name is : {instance.game}')
print(f'Name is : {instance.system}')

print('------------------')
# im writing "class_name".'variable_name'
print(Future.fun)

# im writing "instance".'variable_name'

print(instance.fun)