
userinput=int(input("Enter the N value : "))


def firstPrintNnumbers(num):
    x=0
    while x < num:
       
         x=x+1
         yield x
      

#print(type(firstPrintNnumbers(userinput)))

# for i in firstPrintNnumbers(userinput):
#     print(i)

print(next(firstPrintNnumbers(userinput)))
print(next(firstPrintNnumbers(userinput)))
print(next(firstPrintNnumbers(userinput)))
print(next(firstPrintNnumbers(userinput)))
print(next(firstPrintNnumbers(userinput)))