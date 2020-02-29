# example
# Counting the number of objects of the class 


class Student:
    count=0
    
    
    def __init__(self):
        Student.count=Student.count +1
         
s1=Student()

s2=Student()
s3=Student()
print('the number of students are',Student.count)

s4=Student()
s5=Student()
s6=Student()

print('the number of students are',Student.count)
