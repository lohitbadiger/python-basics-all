def printme(*names):
    print('which data type is added',type(names))
    print('printing the passed arguments')
    for name in names:
        print(name)
# calling the function 
printme(100, 10.09, 'lohit')