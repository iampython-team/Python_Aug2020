
 
def getNumbers(num):
        num=num**2
        print(num)
        yield


genx=getNumbers(4)

try:
    next(genx)
    next(genx)
except StopIteration as si:
     print("exception is thrown ",si)
    