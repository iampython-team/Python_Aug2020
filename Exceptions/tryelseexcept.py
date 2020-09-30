
try:
    r=5/1 # 
except ArithmeticError:
    print("exception thrown")  
# if True:
#     print("hello")
else:
    print("there is no exception")
finally:
    print('always executed')
