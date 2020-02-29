

def names(dictionary):
    for key, value in dictionary.items():
        print(f'At spiceup {key} is handled by {value}')




assignment={}

while True:
    program=input('enter the name of programming Language')
    student=input('enter the student name')
    assignment[program]=student
    another=input('do you want to add one more item (y/n) ')
    
    if another=='y':
        continue
    
    else:
        break
    
names(assignment)