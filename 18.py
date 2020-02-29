store={'name':'lohit', 'age':20, 'job':'spiceup'}

print(store)

print('--------------------------')

print(store['name'])

print(store['job'])


# empty dictionaries 

store={}
print(store)

# assinging the value to the dictionary position 

store['name']='Yuri'
print(store)

store['phone']=98249845
print(store)

print(store['phone'])


x = dict(name = "John", age = 36, country = "Norway")
print(x)



print('-----------------')

tinydict={'name':'lohit','number':2032, 'country':'India'}

print(tinydict)

print(tinydict.keys())
print(x.keys())

print(tinydict.values())


# if i have same key names of a value 1st value will be replaced with latest value 

tinydict={'name':'lohit','number':20302, 'country':'India','name':'yuki'}
print(tinydict)
