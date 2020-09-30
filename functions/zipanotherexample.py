numbers=['one','two','three','four']
num=[1,2,3,4]

z=zip(numbers,num)
x,y=zip(*z)

print(x)
print(y)