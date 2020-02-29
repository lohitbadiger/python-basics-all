# class name:
#     def say(self,name):
#         return name 
    
# class age(name):
#     def talk(self,age):
#         return age
    
# class address(age):
#     def print_this(self,address):
#         return address
    
# ok= address()
# print(ok.say('lohit'))

# # this will give errorr
# do_it=age()
# print(do_it.say(1000))

# full_sentence=address()
# print('hello im',do_it.say('Lohit'),'my age is',do_it.talk(20),ok.print_this('I stay in'), 'Koramanagala')





class Father:
    
    def singer(self, quality):
        return quality
    

class Mother():
    def cook(self,cook):
        return cook
       
class son(Father,Mother):
    def artist(self,son_quality):
        return son_quality
    


class grandSon(son):
    def turist(self,grand_song_quality):
        return grand_song_quality


some_one_talking_to_grand_son=grandSon()

print(some_one_talking_to_grand_son.turist('Turist'))
print(some_one_talking_to_grand_son.singer('singer'))
print(some_one_talking_to_grand_son.artist('artist'))

