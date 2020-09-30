try:
    file=open("Files/python1.txt",'r+') # r-read , w- create and overwrite , a - 
    
    # if file.writable():
    #     print("yes! Writable")
    #     file.write("hello")
        
    if file.readable():
        print("yes! Readable")
        print(file.read())
       

except:
    print("File is not found")
    