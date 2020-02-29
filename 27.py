
# # iterative in list 

a=['dhsjf','adsfhj']
itr=iter(a)
print(list(itr))



# print('--------------------------')


a=['foo','boo','loo']

itr=iter(a)

print(next(itr))
print(next(itr))
print(next(itr))



# print('----------------------')


xyz=['lohit', 'sie', 'daiki']

for name in xyz[0:1]:
    print(name)
    
    
abc=iter(xyz)

print(list(abc))

print('---',next(abc))

# print('---------------------------------------')

# # dict syntax 
# # dict={'index':'value'}

num={'words':'lohit','num':23,'school':'spiceup'}

for k in num:
    print(k)

print('---------------')
    
for v in num.values():
    print(v)

print('---------------')


# i,j=(1,2)
# print(i,j)
# print('---------------')
# x=[(1,2),(3,4),(5,6)]
# for i,j in x:
#     print(i,j)
    

# if i call dict.items it will convert dict into tuple 
print(type(num))
for v in num.items():
    print(v)
print('---------------')
print('---------------')


for v in num.values():
    print('values',v)
    
    
d={'name':'lohit','age':20,'school':'spiceup'}

# keyword items 
for k,v in d.items():
    print('k =',k,'v =',v)


print('---------------')


