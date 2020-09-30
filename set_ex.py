


numbers1={1,2} # set 
numbers2={"one":1,"two":2}  # two values (key,value)
print(type(numbers1))
print(type(numbers2))

evennumbers={2,4,6,8,10,2,4,6,8,10} # set does not stores duplicate values, 
                                    # does not follow insertion order
                                    # set - no index, hashtable 
print(evennumbers)

person={
    "john",
    56,
    "NewYork",
    4000.56,
    True
    
}
# set allows multiple data types 
print(person)
# set is mutable object 



#frozenset - immutable object 

fz=frozenset(person)
print(fz)

fz1=frozenset("hello")
print(fz1)


fz2=frozenset([1,2,3])
print(fz2)


fz4=frozenset((1,2,3))
print(fz4)


#fz5=frozenset(7)
#print(fz5)


# int, float, complex,str, tuple and frozenset - immutable 
# list, set - mutable 


evennumber = {2,4,6,8}
oddnumber={1,4,5,7}
print(evennumber.union(oddnumber))
print(evennumber | oddnumber )

print(evennumber.intersection(oddnumber))
print(evennumber & oddnumber)


# list ---> duplicate, dynamic , index 

# tuple --> duplicate, static,  index 


# set ---> unique, order is not maintained


# tuple - strores duplicate, index 

# frozenset - does not stores duplicate, hashtable