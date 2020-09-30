
int() 
float()
complex()
str()
list()
tuple()
set()
frozenset()
dict() 
bool() 
# functions 
bytearray()
bytes()

# float --> int 
x=4.2
print(int(x))

# float -> complex 
y=4.5
z=6.7
print(complex(y,z))


# int -> string 
g=123 # int 
print(str(g))  # string 

# string - > list
name="India" # str 
print(list(name)) # list 

# list - tuple 
listx=[1,2,3,4,5,6]
print(tuple(listx))

# list - > set 
print(set("raja"))


# int/float - bool
x=set()

# any datatype is 0, or empty - False 
# any value is found - True

# 0 - False, any int - True 
print(bool(x))

print(type({1:'One'}))

# int - dict 
# str - dict 
# list - dict 
# tuple - dict 
# set - dict 

listdata=(
    [1,"one"],
    [2,"two"],   
)

print(listdata)

print(dict(listdata))


s=set([1,2,3,4])
print(s)