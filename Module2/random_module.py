import random


print(random.randint(2,189)) # ValueError: empty range for randrange() (10000, 3, -9997)
#print(random.random()) # 0-1 

listx=(1,3,5,7,9,11,13,'India','Hello',True)
print(random.choice("hello Python Developer"))

print(random.choices(listx))

print(random.random()) # 0-1 
random.seed(4)
print(random.random())
