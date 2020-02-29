#  self parameter 
'''
the self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.  

It does not have to be names self, 
you can call it anything you want to call.

*But it has to be first parameter of any function in the class:
'''


class Subject:
    
    def __init__(anything,working, salary):
        anything.working=working
        anything.salary=salary
    
    def myWork(anything):
        print('if you work as',anything.working,'you get paid',anything.salary)
        
create=Subject('python developer','very good salary')
create.myWork()


