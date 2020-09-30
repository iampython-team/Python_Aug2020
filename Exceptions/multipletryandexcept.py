
try:
    a=5
    print(a)
    
    try:
        r=5/0
    except Exception as ae:
        print('exception name is ',ae)
        
except Exception as e:
    print("name error",e)