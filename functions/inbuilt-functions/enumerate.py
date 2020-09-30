
cities=['Bangalore','Newyork','Rome','Paris']
print(type(cities))



e=enumerate(cities,9)
print(type(e))

#print(list(e))

# list -> enuemrate -> list / tuple/set 

for seq,city in e:
    print(seq,city)
    
    
    
person={
    'name':'John',
    'age':45,
    'city':'NY'
}

dicte=enumerate(person)
print(list(dicte))
