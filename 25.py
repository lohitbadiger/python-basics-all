

# break is opposite of continue 
lists=[1,2,3,4,5,6,7,8,9]


count=1 

for i in lists:
    if i==4:
        print('item is matched')
        
        count=count+10 
        # no more looping after this line
        break
    print('NOW THE NEW VALUE OF COUNT', count)
    
print('the end') 