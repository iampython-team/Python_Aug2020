
try:
    fpointer=open("/Users/SRIRAMAPADMAPRABHA/Desktop/Python_Aug/Files/sunday.txt",'a')
    print("file is succefully created")
    fpointer.write("this is sunday class")
    
except FileNotFoundError:
    print("File is not available")

# first param - file path , second param - mode , encoding - utf-8

