

# # Control statements 
# if 
# else 
# elif 

# # looping 
# for 
# while 

# # simple 

# break
# pass 
# continue 

# ctrl + /  - all selective statements in comment section 


# prob statement - person/ citizen of India - age must >= 18 

#age=int(input("Enter the person's age => "))
age=45

if age >= 18: 
    print('he/she is eligible to vote')
    
else: 
    print('he/she is not eligible to vote')


# prob statement - metro lines 

route=input(" Enter your travel destination (with in the city) ")


if route == 'Jurong East':
    print('This is green line')
elif route == 'Changi Airport':
    print('This is Red line ')
elif route == 'Bisan':
    print("this is yellow line")
    
else: 
    print('MRT (Metro) is not availble in this route')
    


if True:
    print("my name is Raja")

