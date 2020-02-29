# Object Methods 

# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Subject:
    
    def __init__(self, language, greet):
        self.language=language
        self.g=greet
        
    def myDialog(self):
        print('my name is lohit and i teach',self.language,','+self.g)
        
        
var=Subject('Python','Good Morning')
var.myDialog()