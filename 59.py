

message='shdhsjk'

def print_message():
    # the variable 'message' is local to the function itself
    
    global message
    # now message has become global function 
    
    message='hello ! I\'m going to banglore'
    return message

print(print_message())

print(message)
