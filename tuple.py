numbers=(1,3,4,6,2,2,2,2,2,2,2,2,2,2)  # index - 0 -n-1 
numbers2=[1,2,3,4,6]

#numbers[4]=5
#TypeError: 'tuple' object does not support item assignment
print(type(numbers))
print(type(numbers2))

# dynamic data - list - [] - index - data can be modified - stores duplicates - stores multiple data types - mutable 
# static data - tuple - () - index - data cannot be modified -stores duplicates -stores multiple data types - immutable 


# immutable - int, float, complex ,bool, str, tuple 
# mutable - list, set


print(numbers.count(2))

print(numbers.index(2))
