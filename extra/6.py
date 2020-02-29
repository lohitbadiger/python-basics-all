
# Modify Object Properties


# You can modify properties on objects like this:


class Place:
    def __init__(self,trip,price,dist,photo):
        self.trip=trip 
        self.price=price
        self.distance=dist
        self.photo=photo 
        
    def MyTrip(self):
        print('hello im going to',self.trip,self.price)
        # print('hello im going to',self.price)
        # print('hello im going to',self.distance)
        # print('hello im going to',self.photo)
        

    def MyPrice(self):
        print(' im going to pay ',self.price)       
        
MyTrip=Place('India','10,000','5000km','color')
# MyTrip.trip='Japan'
print(MyTrip.trip)
# print(MyTrip.place)
print(MyTrip.price)
print(MyTrip.photo)




print('-----------------------------')

MyPricexx=Place('Paris',2000,'4000km','blue')
# MyPricexx.price=30000
print(MyPricexx.price)