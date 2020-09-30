

# list () 

# [] 

numbers = [1,2,3,4]

t=(1,2,3,4)
listx=list(t)

# list comprehension 

# [ expression for item in items condition ]

for i in numbers: 
    print(i)

n=[ i*2 for i in numbers]
print(n)



game='baseball'

# 
new_game=[ char.lower() for char in game ]
print(new_game)


countries=('Poland','Singapore','India','Srilanka')
countries_upper=[country.upper() for country in countries]
print(countries_upper)



person={
    
    'name':'John',
    'age':45,
    'location':'NY',
    'income':45.2
    
}



person_newform=[ {k,v} for k,v in person.items()]
print(person_newform)


numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

even=[ num for num in numbers if num%2 == 0 ]
print(even)



