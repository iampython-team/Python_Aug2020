# with - 2.5 

# one way 
file=open("File2/one.txt",'w')
file.write("today is Sunday")


# second way - exceptions 

try:
    file=open("File2/one.txt",'w')
    file.write("today is Sunday")
except:
    print('exception is thrown')
finally:
    file.close()
    
    
    
# third way - with 
try:
    with open("File2/one.txt",'w') as file:
             file.write("today is Sunday")
except:
    print('exception is thrown')
    

