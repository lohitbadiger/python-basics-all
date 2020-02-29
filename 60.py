# # calculating with *args

# def calculate(*args):
#     print(sum(args))
    
# calculate(10,30)

# # one more way  


# def calculate(*args):  
    
#     sum=0  
#     for arg in args:  
#         sum = sum +arg  
#     print("The sum is",sum)  
# sum=0  

# calculate(10,20,30,50) #110 will be printed as the sum  
# print("Value of sum outside the function:",sum) # 0 will be printed  


def names(**kwargs):
    return kwargs
# this will give the dict valus as output
print(names(names='lohit', age='age',x=20))