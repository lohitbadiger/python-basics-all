class planet:
    
    shape='round'

    @classmethod 
    def commons(cls):
        return f'All the planets are {cls.shape}'
    
    
    @staticmethod
    def spin(speed='200 m/s  speed'):
        return f'earth speed is {speed}'



print(planet.commons())

print(planet.spin('60000m/s'))
# even this will also print 
print(planet.spin())

