

student={
    
    'name':'John',
    'age':17,
    'marks':{
        'maths' :75,
        'Physics' :84,
        'English' :93,
    }
    
    
}

print(student)


# retreive all keys fron dict 
print(student.keys())

# retreive all values fron dict 
print(student.values())

# # retreive all items fron dict 
print(student.items())

# adding the new key to existing dict 
student['location']='Mumbai'

student['class']='11th Class'
print(student)


student['age']=14
print(student)

# copy of same dict data into new dict 
student1=student.copy()
print("student 1 :", student1)

# get  an element value fron dict 
# one way 
print(student.get('name'))

# another way 
print(student['name'])


s1={
    'name':'Raja',
    'age':24,
    'm%':56
}

s2={
    'name':'john',
    'age':23,
    'location':'Bangalore'
    
    
}

s1.update(s2)
print(s1)





# from keys - creates new dict from the given sequence elements with value 
cities={'Mumbai','Bangalore','Chennai','Jaipur'}
country="India"
c=dict.fromkeys(cities,country)
print(c)



# delete all the items from the dict 
student.clear()
print(type(student))
