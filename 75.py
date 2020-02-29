
# # simple sum program

# def total(a,b):
#     return a+b 
    
# print(total(10,20))

# # implemente fun that takes list as parameter and returns the first item of the list 


# def lis(mylist):
#     return mylist[0]

# ok=[1,2,3]
# print(lis(ok))


# # implemente fun that takes list as parameter and returns the last item of the list 
# def lis(mylist):
#     return mylist[-1]

# ok=[1,2,3]
# print(lis(ok))


# # implemente fun that takes list as parameter and returns the first and last item of the list 
# def mylist(takes):
#     return takes[0],takes[-1]
# take=[1,203,32,323]

# print(mylist(take))


# #  List Maximum
# def foo(mylist):
#     return max(mylist)
# my=[1,2,3,4,5,6]
# print(foo(my))

# # List Concatenation
# def foo(lst1,lst2,lst3):
#     first=lst1
#     second=lst2
#     three=lst3
    
#     return first+second+three

# print(foo([1,2],[3,4],[5,6]))
    

# # Question 1:
# # What would the following function return? Please answer it mentally, without running the code on your Python interpreter.
# # tell the output
# def foo(*args):
#     return args * 2
 
# print(foo("john", 4, "marry", 5))

# Coding Exercise 14: Multiple Arguments Call

# # edit 67th line so that o/p is [2,6,10]

# def foo(*args):
#     double_list = [x*2 for x in args]
#     return double_list
    
# print(foo(1,2,3))


# def foo(*args):

#     return list(args)
#         # i want output like [1,'a',5,'c']
# # print(foo(1,'a',5,'c'))

# # multiple inputs and retuns dict 

# def foo(**kwargs):
#     return kwargs

# print(foo(a=1,c=5,d=109))

# print('---------------------------------------------')

# # takes indefinate numbe of lists and return the concatenated list 
# # for exmple 
# # foo([1,2],[3,5,6,8],[1])
# # it should return [1,2,3,5,6,8,1]

# def foo(*ars):
#     ls=[]
#     for each in ars:
#         ls=ls+each
#     return ls
# ok=[1,2]
# ok1=[3,5,7,8]
# ok2=[1]


# print(foo([1,2],ok1,ok2))



# print('---------------------------------------------')

#18  True if All

# def num(*args):
#     for a in args:
#         return a
# ok=[1,2]
# ok2=[3,4]

# print(num(ok,ok2))


# a=10
# if a:
#   print("List is empty")

# indefinate input list 
# item is present true else false 


# def foo(*args):
#     for a in args:
#         if a:
#             if len(a)==0:
#                 return 'False'
                
            
#             elif len(a)!=0:
#                 return 'True'
            
#         else:
#             break

# first=[1,2,3]
# second=[4,5,6]
# three=[5,6]
# print(foo(first,second,three))

def number(**kwargs):
    
    return list(kwargs.values())
    for a in list(kwargs.values()):
        if a:
            if len(a)==0:
                return 'False'
                
            
            elif len(a)!=0:
                return 'True'
            
        else:
            break 
    



    # return list(kwargs)

print(number(name=[1,2,3],x=[4,5,6],y=[5,6]))