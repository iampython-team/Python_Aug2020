
var1=int(input("Enter varaiable 1 "))
var2=int(input("Enter varaiable 2 "))

def SumSquareDecor(function):
    x=3 
    print("x is ",x)
    def inner():
        final_result=function(var1,var2)**2
        print(final_result)
        #return final_result
    return inner()

@SumSquareDecor
def sum2(a,b):
    res=a+b
    return res 

