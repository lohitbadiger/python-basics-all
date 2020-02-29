# # classmethod in python 
# The class method in Python is a method, which is bound to the class but not the object of that class. The static methods are also same but there are some basic differences
class Planet:
    
    shape='square'
    
    def __init__(self, water, moon):
        self.water=water
        self.moon=moon
        
        
    def orbit(sei):
        return f'{sei.water } and satellite is {sei.moon}'
    
    
    @classmethod
    def commons(cls):
        return f'all the planets are {cls.shape}'
    
naboo=Planet('yes','moon is not present')
print(Planet.shape)



print(Planet.commons())

print('-----------------------')

print(naboo.orbit())