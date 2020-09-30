
# try  -  multiple except 

try:
    a=5
    b=0
    c=a/b
    print('Result ',c)
    
except (ZeroDivisionError,NameError) as e:
    print('Exception is ',e)
    
# except ZeroDivisionError as z:
#     print("exception name is ",z)
    
# except NameError as ne:
#     print("exception name is ",ne)


    