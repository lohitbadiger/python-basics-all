# object methods 

# objects can also contain methods. 
# methods are kind off functions 
# the functions belongs to the class 


class Subject():
    
    
    def __init__(self, language,greet):
        self.language=language
        self.greet=greet
        
    def MyDialog(self):
        
        print('I can speek ',self.language)
        print('I wish you a ',self.greet)

    def MyDialog1(self):
        
        print('I can speek ',self.language)
        print('I wish you a ',self.greet)
          
        
instance=Subject('English','Good Morning Guys')
print(instance.language)

instance.MyDialog()

instance1=Subject('Japanse','Good Morning Guys')

instance1.MyDialog1()



class Dog():
    
    def __init__(self,name):
        self.name=name 
        
    def talk(self):
        print('hello my name is ', self.name)
        
        
ok=Dog('dogs')

print(ok.name)


ok.talk()
