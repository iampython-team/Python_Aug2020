
# map(function, seq)
# reduce 
# filter

# square the every element of the list
listx=[1,2,3,4,5,6,7,8,9,10]

# option 1
for i in listx:
    print(i*i)

# option 2  map with lamda 
print(list(map(lambda x:x*x,listx)))


# option 3 mapy with out lamda 

def squareElement(n):
        return n*n
    
l=map(squareElement,listx)
print(list(l))


names=['italy','india','russia','france']

output=[]

for name in names:
    output.append(name.upper())
    
print(output)


print(list(map(lambda name: name.upper(),names)))


def getUpperNames(name):
    return name.upper()

print(set(map(getUpperNames,names)))


# for, map , lamda , def 



# first name and last name 
# john doe 
# 2 and 2 = jodo@fb.com 

    