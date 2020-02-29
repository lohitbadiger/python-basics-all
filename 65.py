class Person:
    def __init__(ok,name,id,school):
        ok.name=name 
        ok.id=id
        ok.school=school 
         
    def myFunction(good):
        print('hello my school name is',good.name,'my id is',good.id,'im graduate at',good.school)
        
create_instance=Person('KLETECH','290','Graduate')

create_instance.myFunction()