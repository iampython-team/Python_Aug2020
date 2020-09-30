

def outer():
    a=5
    b=6
    #return a+b
    
    def inner():
        s=3
        return s**5
    return inner()
    
res=outer()
print(res)


        