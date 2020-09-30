
s1="india2020$560=}" #  "raja '2020' "
s2='india2020$560=' # 
s3='''india2020$560= ''' # doc string, multiline comment 

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))


firstname="Sachin"
middlename="Ramesh"
lastname="Tendulkar"

print(firstname+" "+middlename+" "+lastname)

print(3*(firstname+lastname))


country='India'

# indexing []
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])
# print(country[5]) IndexError: string index out of range

print(country[-1])
print(country[-2])
print(country[-3])
print(country[-4])
print(country[-5])

# slicing [startindex:stopindex]
print(country[0:2])  # I  0 n -1 d -2 i -3 a 4

print(len(country))


a="python"
print(a[::-1])






