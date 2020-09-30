file3=open('File2/mars.txt','r')

tuplex=['orange is a fruit','Jasmine is flower']
file3.writelines(tuplex)

print(file3.writable())

# empname - [] --> text csv 


# write - allows to write a string data 
# writelines - allows you to write string and list


# r - which is deafult mode for file 


# FileNotFoundError: [Errno 2] No such file or directory: 'mars.txt'





# writable/ write  -str  / writelines - str/list
# readable /read/ readline - str (fist line )/ readlines   - str/list 

file3.close()

if file3.closed: 
    print("yes it is closed ")
else: 
    print("no it is not closed")