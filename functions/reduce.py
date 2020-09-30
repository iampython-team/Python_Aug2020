#reduce(function,seq)
# filter(function,seq)

#import functools

from functools import reduce,lru_cache,cmp_to_key

numbers=(1,2,3,4,5,6,7,8,9,10)

emty_list=[]
for num in numbers:
    if num % 2 ==0:
      emty_list.append(num)
      
print(emty_list)
    

print(list(filter(lambda x: x%2==0,numbers)))


def evenfilter(n):
    if n%2 == 0:
        return n
    
print(list(filter(evenfilter,numbers)))



# [11,12,13,14,15]
# sum of square of even numbers - filter / map / reduce 


listx=[1,2,3,4,5]

result=reduce(lambda x,y: x+y,listx)
print(result)