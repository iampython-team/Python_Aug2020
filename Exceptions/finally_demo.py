import os

try: 
    a=5
    b=0
    os._exit(0) 
    result=a/b
      # 1 0 
except: 
    print("Exception is thrown")
   
finally:
    print(8+16)