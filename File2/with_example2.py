
file=open("File2/twotwo.txt",'w')
file.write("today is Friday")

print(file.closed)  # false 


with open("File2/twotwo.txt",'w') as file:
    file.write("today is Friday")
    
print(file.closed)
