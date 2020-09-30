
news_title="india won the match match match"

print(news_title.title())
print(news_title.upper())
print(news_title.lower())
print(news_title.capitalize())
print(news_title.casefold())

# gmail : login and password  --  RAJA2020@gmail.com - lower ()  
# raJA2020@gmail.com casefold() 

little_text='baseball' # 8 
print(little_text.center(12,"+"))  # 11 -8 = 3 * = 2*L 1R 

print(news_title.find('Match')) # str is not found .. -1 
print(news_title.count('match',2,4)) # str is not found .. 0 
print(news_title.index('match')) # str is not found ... throws an exception


sports="tennis2020"
print(len(sports))
print(sports.count('tennis',6,47))  # int 

print(sports.isalnum())  # true - alpha num 
print(sports.isalpha())  # true -alpha

phonenumbers='9611112233' # int -> str 
# mobile=str(phonenumbers)
# print(len(mobile))

print(phonenumbers.isdigit())  # validating phone


firstname="hello"
lastname="python"

print("%%".join(firstname)) # + 

# how to reverse a string ? 

# 5-6 ways


river='baseball'
print(river[::])





