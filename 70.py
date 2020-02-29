class human():
    def __init__(self,hand,leg):
        self.x=hand
        self.y=leg 
        
    def part(self):
       
        print('part of body is',self.x)
        print('part of body is', self.y)
        print('-----------------------')
        
        x='right hand'
        y='left hand'
        print('this is ', x)
        print('this is ', y)
        
        xyz=100
        abc=100
        total=(xyz+abc)
        print(total)
        
ok=human('right-hand', 'left-hand')
# calling the instance 

ok.part()