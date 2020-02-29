# map(fun, data)

# this program shuffle the words that are sent to it 

from random import shuffle

def jumble(word):
    changer=list(word)
    shuffle(changer)
    
    return '-'.join(changer)

words=['lohit','sie', 'daiki']

changer=[]

# for word in words:
#     changer.append(jumble(word))
    
# print(changer)

print('------------------------------')

changer = [jumble(word) for word in words]

print(changer)
