#  simple_interest(p, t, r)
# formulae

# Simple Interest = (principal) * (rate) * (# of periods)


def simple_interest(p,t,r):  
    return (p*t*r)/100  
print(simple_interest(t=10,r=10,p=100))

print('----------------------------------')

def simple_interests(p,t,r):  
    return (p*t*r)/100  
p = float(input("Enter the principle amount? "))  
r = float(input("Enter the rate of interest? "))  
t = float(input("Enter the time in years? "))  
print("Simple Interest: ",simple_interests(p,r,t))  

