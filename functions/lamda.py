#lambda parameter_list: expression

var=lambda x: x**2
print(var(4))


addition=lambda a,b: a+b
print(addition(4,5))


def addition(a,b):
    return a+b

print(addition(4,5))






expr=lambda p,q,r,s,t=16 : p+q-r+(s*t) # required / default
print(expr(4,5,5,2))


printnames=lambda *names: len(names) # variable length args
print(printnames('raja','john','trump'))


lang=lambda **languages: languages # KWARGS - KEYWORD ARGS
print(lang(India=['Hindi','Tamil','Bengali','Kannada'],USA='English',Italy='Italian'))



# lamda / map-reduce- filter 






def filterEvenOdd(num):
 for n in num:
    if n%2 == 0:
        print(n,"is even number")
    else: 
        print(n,"is odd number")


numbers=[1,2,3,4,5,6,7,8,9,10,True]

filterEvenOdd(numbers)

# lamda, map/ reduce/ filter 
var=lambda  x: x%2== 0 
print(var(125))
