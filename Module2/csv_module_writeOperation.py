# tesla 
import random
import csv
customer1={
    
    'cus_number': random.randint(1,99),
    'cus_name':'John',
    'cus_location':'NY',
    'offer_price': 20.4  
    
}
 
customer2={
    
    'cus_number': random.randint(1,99),
    'cus_name':'Robert',
    'cus_location':'TX',
    'offer_price': 56.4  
    
}
  
customer3={
    
    'cus_number': random.randint(1,99),
    'cus_name':'Trump',
    'cus_location':'WD',
    'offer_price': 89.4  
    
}


with open('Module2/tesla_car_customers.csv','w') as csv_file:
    data_fieldnames=['cus_number','cus_name','cus_location','offer_price']
    writer=csv.DictWriter(csv_file,fieldnames=data_fieldnames)

    writer.writeheader()
    
    writer.writerow(customer1)
    writer.writerow(customer2)
    writer.writerow(customer3)
     