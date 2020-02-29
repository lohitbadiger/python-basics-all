# printing the value from class based variable 

class Employee:
    # class based var
    id=900.00
    name='John Com'
    
    def display(sei):
        # print('Employee Id is',sei.id, 'Employee name',sei.name)
        
        
        # %d=> int %f=>float %s=>string
        print("ID: %f \nName: %s"%(sei.id,sei.name))
emp=Employee()
emp.display()