# nested for condition 

adj=['red', 'blue', 'white','orange']
fruits=['apples','bananas','cherry','grapes']

for x in adj:
    for y in fruits:
        print('--',x,y)
        
        
print('---')
for i in range(3,20,3):
    quotient=i/3
    print(f'{i} divided by 3 is  {int(quotient)}')