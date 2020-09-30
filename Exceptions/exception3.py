
try:
    a=5
    b=0
    result=a/b
    print(result)
except ZeroDivisionError as ze:
    print("Zero Division error",ze) 
except Exception as e:
    print("Exception is ",e)
