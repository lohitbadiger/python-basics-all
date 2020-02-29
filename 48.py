# def shut_down(s):
#     if s=="yes":
#        return "Shutting down"
#     elif s=="no":
#        return "Shutdown aborted"
#     else:
#        return "Sorry"
# s="nos"
# x=shut_down(s)
# print(x)


print('------------------------------------------------------')
#######################################################


# Simple Python program to find sum of series 
# with cubes of first n natural numbers 

# Returns the sum of series  

# 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225
# def sumOfSeries(n): 
#     sum = 0
#     for i in range(1, n+1): 
#         sum +=i*i*i 
          
#     return sum
  
   
# # Driver Function 
# n = 2
# print(sumOfSeries(n)) 


#######################################################
# from math import sqrt
# print (sqrt(13689))

##################################################

# def distance_from_zero(num):
#     if type(num)== int or type(num)== float:
#         return abs(num)
#     else:
#         return "Nope"
# x=distance_from_zero(-9.6)
# print(x)
# y=distance_from_zero("what?")
# print(y)


#######################################################

def cube(number):
    return number*number*number

def by_three(number):
   if number %3 ==0:
      return cube(number)
   else:
      return False
x=by_three(27)
print(cube(x))

print('------------------shopping_list-------------------------')


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15  
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total=0
    for x in food:
        price= prices[x]
        if stock[x]>0:
           total=total +price
           stock[x]=stock[x] -1
    print(total)

compute_bill(shopping_list)



# def temperature(t):
#     def celsius2fahrenheit(x):
#         return 9 * x / 5 + 32

#     result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" 
#     return result

# print(temperature(20))