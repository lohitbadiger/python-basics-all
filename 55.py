def person(dictionary):
    belts=list(dictionary.values())


    for belt in belts:
        num=belts.count(belt)
        print(f'there are {num} {belt} belts')


lohit_items={}

while True:
    
    lohit_belt=input('enter the name of belt')
    lohit_belt_color=input('enter the color of belt')
    
    lohit_items[lohit_belt]=lohit_belt_color
    another=input('enter another item (y/n)')
    
    if another=='y':
        
        continue
    else:
        break
    
person(lohit_items)