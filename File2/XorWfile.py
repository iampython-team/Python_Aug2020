

# w and x - create a new file if it is not exist 
# x - if file is already exist then it will throw an error 
# w- if file is already exist then it will overwrite 

file=open("File2/sample.txt",'w')

print("file is scuccesfully created")

stringtext='''
# w and x - create a new file if it is not exist 
# x - if file is already exist then it will throw an error 
# w- if file is already exist then it will overwrite 
'''

file.write(stringtext)

file.close()