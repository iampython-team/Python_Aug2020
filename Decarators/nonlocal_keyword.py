# local, global --- Keywords 
# locals(), globals() - Functions 

y=10 # y is global variable


def outer():
    z=15 # z is enclosed variable  
    global y
    print('global variable is ',y)
    y=y+3
    print('after changes ',y) # UnboundLocalError: local variable 'y' referenced before assignment
    
    def inner():
        x=4 # x is local variable
        global y 
        y=y+8  #UnboundLocalError: local variable 'y' referenced before assignment
        print('in inner function',y)
        
        nonlocal z
        z=z+9
        print("enclosed change variable - ",z) #nboundLocalError: local variable 'z' referenced before assignment
        
        
        
        
    inner()
    
outer()
y=y+4
print(y)