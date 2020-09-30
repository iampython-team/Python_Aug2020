import random 
import time 

regions=['ASIA','AFRICA','EUROPE','NORTHAMERICA']
countries=['India','SouthAfrica','Norway','Canada']

def people_list(num):
     people_box=[]
     for i in range(num):
         person={
             'id':i,
             'region':random.choice(regions),
             'country':random.choice(countries)
             
         }
         people_box.append(person)
     return people_box
 
def people_generator(num):
    for i in range(num):
         person={
             'id':i,
             'region':random.choice(regions),
             'country':random.choice(countries)
             
         }
         yield person
         
         
t1=time.perf_counter()
people_through_list=people_list(100)
t2=time.perf_counter()
print('Time taken for the list : ',t2-t1)
#print(people_through_list)

t3=time.perf_counter()
people_through_generator=people_generator(100)
t4=time.perf_counter()
print('Time taken for the generator : ',t4-t3)
# for each_person in people_through_generator:
#     print(each_person)