class Place:
    def __init__(self, trip, price,dist, photo):
        self.trip=trip
        self.price=price
        self.dist=dist
        self.photo=photo
    
    def MyTrip(self):
        print('hello im going to ', self.trip,self.price)
        
        
    def MyPrice(self):
        print('im going to pay',self.price)
        
myTrip=Place('India','10,000','60000km','color')      
print(myTrip.trip)

myTrip.trip='japan'
print(myTrip.trip)
