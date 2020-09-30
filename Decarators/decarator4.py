def div_decarator(function):
    def inner(x,y):
        if y==0:
            return "y value should not be zero"    
        return function(x,y) 
    return inner

@div_decarator
def div1(a,b):
    return a/b # b should not be zero

print(div1(5,0))
print(div1(5,2))
print(div1(5,))