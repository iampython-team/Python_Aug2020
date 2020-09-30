
# Amazon delivery boy -- moto cycle 
# Bangalore ---  MG road, Bigrade Road, JC road .... 

places={'MG Road','JC Road','Brigade Road','Majestic'} # set

print(places)

for delivery_place in places:
     print(delivery_place+"=========")
     
     
country_name='SouthAfrica'
for char in country_name:
    print(char)
    
# for --- string, list, tuple, set ,range -- sequence 
# for -- dict  - key and value 

person={
    'name':'John',
    'age':45,
    'location':'NewYork'
}

for key,value in person.items():
    print(key,"=========>",value)
    
    
for value in person.values():
    print(value)
    
for key in person.keys():
    print(key)
    
numbers=(1,2,3,4,4,4,4,4,4,4,4,4,4,4,)
for i in numbers:
    print(i)
    
    
dup_prime={2,3,5,5,2,11,13,17,13}
print(dup_prime)

fz=frozenset(dup_prime)
print(fz)

for value in fz:
    print(value)
    
    
for char in "hello, good Evening":
    print(char.upper(),end=" ")
    
    
# hacker rank - python challenge 