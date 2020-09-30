# int  age 
# float income 
# string  name 
#       -4    -3   -2     -1   BWD <-
person=['john',25,400.46,'john'] 
 #        0     1   2      3   FWD <-
print(person)
print(type(person)) 
# list - can store hetero 
# list - same dataype 
# list - [] 
# list - allows duplicates 
# list - indexing 

print(person[-2]) #IndexError: list index out of range

fruits =['banana','apple','watch','jackfruit','orange',]
#          0        1       2       3           4 
fruits[2]='mango' # item assignment 
print(fruits)
# list is mutable 


# int, float, complex and string are immutable 
# list - mutable 


evennumbers=[2,4,6,8,10]
oddnumbers=[1,3,5,7,9]
print(evennumbers+oddnumbers)

print(evennumbers*4)
print("raja"*4)

