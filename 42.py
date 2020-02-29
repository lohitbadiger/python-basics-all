# # function functions with some parameters/arguments 

# def students(name, classes):
#     print(f'helllo im {name}, im new to this class of {classes} ')
    
#     print('Hello', name, 'what are you doing in this class',classes)
    
#     # passing some parameters 
    
# students('lohit','python')

# print('-------------------------------------')


# /////////////////////////////////////////
# def f():
    
#     def g():
#         print("Hi, it's me 'g'")
#         print("Thanks for calling me")
        
#     print("This is the function 'f'")
#     print("I am calling 'g' now:")
#     g()

    
# f()

# /////////////////////////////////////////

# def temperature(x):
#     print(9 * x / 5 + 32)

    
# temperature(10)

#######################################################


#  every parameter of a function is a reference to an object and functions are objects as well, we can pass functions - or better "references to functions" - as parameters to a function.


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print('something is',func.__name__)
         
f(g)
