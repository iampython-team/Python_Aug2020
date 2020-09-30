
sport='baseball'
# string --> basetall
#sport[4]='t' #TypeError: 'str' object does not support item assignment

print(sport)

# immutable object 
sport='basetall'
print(sport)


#immutable dataypes - int, float, complex, string 

# String interpolation - String formmating 
# 4 ways - %, format, sys.format() , f-strings (from 3.6)

name="raja" #input("Enter your name :")
age= 45 #int(input("Enter your age : "))
print(f'Hello,{name} - Good Evening!! Your age is {age} ')
print(f'hello 2020')

x=56
y=78
print(f'adding x and y is { x*y }')


# '',""

# realtime project - CSV '''
# 

# triple - double - single 
print(''' John asked "what's there?" ''')

# single - double - single 
print('John asked "what\'s there?" ')  # throwing an erorr

# double - double -single 
print("John asked \"what's there?\" ")  


stringformat1="{}  {}  and {} ".format(True,False,True)
print(stringformat1)

hdfcfacevalue=19.89034567
print('the value of hdfc share %.16f' %hdfcfacevalue) # format 
print('the value of hdfc share %d' %hdfcfacevalue) # format 


print(int("2"))
#print(int("a2"))

a=True  # 1 
b=False  # 0 
c=True # 1
print(a+b+c+a)




