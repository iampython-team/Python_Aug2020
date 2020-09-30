import datetime,time,calendar


#datetime - module 
# date , time, datetime ,timedleta,tzinfo,timezone 
#12AM 1st JAN 1970 
# ticks since 1970 
print(time.time())

# local time 
print(time.localtime(time.time()))

#format time 
print(time.asctime(time.localtime(time.time())))

for i in range(0,5):
    print(i)
    time.sleep(0.1)


print(datetime.datetime.now())
print(datetime.datetime(2020,12,31,11,59,59))

#comparison two dates 
d1=datetime.datetime(2020,12,31,11,59,59)
d2=datetime.datetime(2020,1,2,11,59,59)
#print(type(d1-d2))
#print(str(d1-d2))
new_delta_value=str(d1-d2)
l=new_delta_value.split()
print(l[0])


twentytwenty=calendar.prcal(2020)
print(twentytwenty)



