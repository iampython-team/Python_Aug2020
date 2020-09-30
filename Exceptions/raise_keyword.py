from lib2to3.pytree import Base


try:
    age=int(input("Enter your age : "))
    
    if(age <18):
        raise ValueError  # python exception 
    else:
        print('Age is valid and age is ',age)
        
except ValueError:
    print("Age is not valid")
    
# insurance - UW = AXA - AXAUWException 
# banking - amount limit 

class AXAUWException(BaseException):
    pass
