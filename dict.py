# bank

customer={
    'name' : 'john',  # str 
    'age':47,  # int 
    'amount':4500.56,  # float 
    'address':['RES ADD','OFC ADD'],  # list 
    'languages':('English','French','Italian'),  # tuple
    'education': {'B.Tech','M.Tech'}, # set 
    'American':True,  # bool   
    'loans':{
        'home_loan':45,
        'personal_loan':10,
    },
    'c':4+5j # complex
  
}


print(customer)
print(customer.keys())
print(customer.values())

print(customer['amount'])
print(customer['languages'][1])
print(customer['loans']['personal_loan'])
print(customer['education'])

