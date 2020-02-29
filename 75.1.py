
# we have a class defined variables. 


# Exercise
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
class Vehical:
    name=''
    kind='car'
    color=' '
    value=''
    
    def description(self):
        desc_str=("%s is a %s %s worth $%.2f "% (self.name, self.color,self.kind,self.value))
        return desc_str
    
    # instance
car1=Vehical()
car1.name='Fer'
car1.kind='convertable'
car1.color='red'
car1.value=60000.00
print(car1.description())

car2=Vehical()
car2.name='Jump'
car2.kind='convertable'
car2.color='blue'
car2.value=100000.00
print(car2.description())


car23=Vehical()
car23.name='Jump'
car23.kind=''
car23.color=''
car23.value=100000.00
print(car23.description())