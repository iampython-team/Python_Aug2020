
class Customer():
    bankname='DBS'    
    # constructor 
    def __init__(self,name,accountnumber):
         self.name=name
         self.accountnumber=accountnumber
    
    # instance method 
    def deposit(self,amount):
        self.amount=amount # self.amount - instance variable 
        print(self.amount)
    
    # instance method 
    def withdraw(self): 
         print(self.accountnumber)
         print(self.amount)
    
    # class method 
    @classmethod
    def getCustomerDetails(cls):
        print(cls.bankname) 
    
    # static method 
    @staticmethod
    def getBankDetails():
        pass 
    

c1=Customer('john',12345)
c1.deposit(3000)
c1.withdraw()

Customer.getCustomerDetails()