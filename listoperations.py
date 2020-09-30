
listx=['Poland','Singapore','India','Norway','Norway','SouthAfrica','Singapore']
        # 0      1           2        3        4

southAmerica=['Chile','Peru']

# insertion functions or operations 
listx.insert(3,'Nepal')  # only one item or object can be added at given postion of list
print(listx)

listx.append('Uganda')   # only one item or object can be added at end of the list
print(listx)

listx.extend(southAmerica) # multiple items can be added. Item must be an iterable object
print(listx)
# update functions 
new_list=listx.copy()
print(new_list)


# delete functions 

#listx.clear()  # clear all the data from the list
#print(listx)

listx.pop()
print(listx)

listx.remove('Norway')
print(listx)



# support or other functions 

print(listx.index('India'))

print(listx.count('Singapore'))



listx.sort()
print(listx)

numbers =[True,False,True,False,False,False,True]
numbers.sort()
print(numbers)

listx.reverse()
print(listx)


prime_numbers=[3,5,23,2,11,7,19,13]
prime_numbers.sort(reverse=True)  # sort --> reverse 
print(prime_numbers)