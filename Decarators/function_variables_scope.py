a=3 # global variable
g=9
def test():
    a=5  # enclosed variable / inner function variable
    b=8
    print('a in test',a)
    def innerTest():
        a=7 # local variable 
        print("g (global variable ot module) ",g)
        print('b (outer function)is ',b)
        print('a in innerTest',a)
    innerTest()
    
test()
        
        
print(dir())


        
        
    