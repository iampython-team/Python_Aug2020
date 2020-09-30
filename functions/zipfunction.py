empty=zip()
print(empty)
print(type(empty))


countries=['Italy','Poland','Belgium','Sweden','Austria','India','Singapore']
dailingCodes=['+39','+48','35','+45',None,'+91','+65']
continent=['Europe','Europe','Europe','Euorpe','Europe','Asia','Asia']
tuplex=(1,2,3,4,5,6,7)
stringx="hello"


z=zip(countries,dailingCodes,continent,tuplex,stringx)

#print(list(z))  # unzipping -1 


# for  data in z:   # for -2 
#     print(data)


print(*z) #-3 


x=(1,2,3)

print(list(zip(x)))


