# what are the first-class objects

# syntax 
# def functionname(argumentlist / paramlist ): 
#     # logic 


# simple function 
def getInfo():
    print("hello, this is python programming")
    
getInfo()

# params 
def addition(a,b,c=6,):
    result=a+b+c
    return
    
print(addition(4,5))

# True/False None 

# parameters 

# 1. Default - c 
# 2. Required/ Positional Required Args   - a and b 
# 3. * - vargs variable length args 
# 4. ** - KWARGS - keyword length args

def getEname(*names):
        print(type(names))
        return names
    
    
# ename (object type)
# 100 - 90 string  10 None 

print(getEname('Raja','John','Robert','Donald','Trump',2020,2019,2018,True))



# keyword args
def person(firstname,lastname,age,*addresses,location='NY',**experinces,):
    print(firstname+lastname)
    print(age)
    print(location)
    print(addresses)
    print(experinces)
    
person('Joh','Doe',45,'Res','Ofc','FORIDA',fistfive='google',secondfive='twitter')

    
