# The self Parameter
'''
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


'''

# Use the words 'AnythingFine' and 'abc' instead of self:

class Subject:
    def __init__(AnythingFine, working, salary):
        AnythingFine.ok=working
        AnythingFine.sal=salary
    
    def myWork(AnythingFine):
        print('Hello my work',AnythingFine.ok)    
       
submit=Subject('"It is Great"','poor')
submit.myWork() 




