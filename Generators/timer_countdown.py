import time 


def countdown(number):
    print(" count down starting ...... ")
    while number > 0:
        yield number
        number=number-1
        
        
countvalue=countdown(10)


for eachnumber in countvalue:
    print(eachnumber)
    time.sleep(2)