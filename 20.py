
# # tup=('w',4,4)
# # pr    int(tup)

# # print(tup.delete('w'))

# tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
# print(tuplex)
# #tuples are immutable, so you can not remove elements
# #using merge of tuples with the + operator you can remove an item and it will create a new tuple
# tuplex = tuplex[:2] + tuplex[3:]
# print(tuplex)
# #converting the tuple to list
# listx = list(tuplex) 
# #use different ways to remove an item of the list
# listx.remove("c") 
# #converting the tuple to list
# tuplex = tuple(listx)
# print(tuplex)



# # d = {0:10, 1:20}
# # print(d)
# # d.update({2:30})
# # print(d)

# # d.update({'name':"lohit"})
# # print(d)
# # # Write a Python script to merge two Python dictionaries.


# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# print(d1)
# d = d1.copy()
# print(d)
# d.update(d2)
# print(d)

#  Creating an empty Dictionary 
# Dict = {} 
# print("Empty Dictionary: ") 
# print(Dict) 
  
# # Creating a Dictionary  
# # with Integer Keys 
# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
# print("\nDictionary with the use of Integer Keys: ") 
# print(Dict) 
  
# Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
  
# # Creating a Dictionary 
# # with dict() method 
# Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
# print("\nDictionary with the use of dict(): ") 
# print(Dict) 
  
# # Creating a Dictionary 
# # with each item as a Pair 
# Dict = dict([(1, 'Geeks'), (2, 'For')]) 
# print("\nDictionary with each item as a pair: ") 
# print(Dict) 