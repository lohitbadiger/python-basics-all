# defining a funtion 

# def change_list(list1):
#     list1.append(20)
#     list1.append(30)
#     print('list inside the function =',list1)
    
# list1=[10,20,30,40,50]

# change_list(list1)
# print('list outside funtion is=',list1)



print('-------------------------')

def change_string(str):
    
    str=str+'how are you?'
    print('printing the string inside the function:',str)
    
string1='Hi my name is lohith'

# calling the function
change_string(string1)
print('this is outside',string1)