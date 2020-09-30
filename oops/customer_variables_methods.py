x=5
# class (static), instance (object) and local 
# instance method (object), class and static 

# class/static  variable - class method 
                          # static method 
# insatnce varaible / instance method 
# local variable 


#insurance --policies - vehicle 

#1000 customers - 1000 - premium 

class Customer:
    
    # class variable 
    bankName='HSBC'  # can access by class name and object reference 
    
    # constructor 
    def __init__(self,cname,caccountnumber): 
        self.customer_name=cname  # instance variable 
        self.customer_accountnumber=caccountnumber # instance variable 
        print(Customer.bankName,x)
        
    def __init__(self,cname,caccountnumber): 
        self.customer_name=cname  # instance variable 
        self.customer_accountnumber=caccountnumber # instance variable 
        print(Customer.bankName,x)
     
    #instance method    
    def displayCustomerInfo(self):
        branchname='NY branch' # local variable 
        print('Customer information')
        print("============")
        print(self.customer_name)
        print(self.customer_accountnumber)
        print(Customer.bankName,x,branchname)
    
    @classmethod
    def getBankName(cls):
        print(cls.bankName)
        
    @staticmethod  
    def getCustomerCount():
        # select count(customer_number) from customer
        count=55
        
        print(count)
        print(Customer.bankName)
        
           
c1=Customer('John',12345)   # invoking the constructor and calling the object 
c1.displayCustomerInfo()  # accessing the instance method by the object reference 

print("outside of class",Customer.bankName) #class variable can be accessed through class name 
print("accessing the class variable through object reference",c1.bankName) #class variable can also accessed through object reference

Customer.getBankName() # class method can be accessed through class name 
c1.getBankName() # class method can also accessed through object reference 



Customer.getCustomerCount()
c1.getCustomerCount()