def area(radius):
    return 3.142 *radius*radius


def volume(area,length):
    print(area*length)
    
radius=int(input('enter the radius')) 
length=int(input('enter the length'))

volume(area(radius), length)

