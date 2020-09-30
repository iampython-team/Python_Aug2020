
# TV

# properties - TV brand , TV size, modelname, model year 
# methods  - view, .....

class TeleVision:  #class TeleVision(object):
    
    ''' this is about television class '''
    
    #constructor
    def __init__(self,brand,size,modelname,modelyear):
        print("calling constructor ")
        self.brand=brand
        self.size=size
        self.modelname=modelname
        self.modelyear=modelyear
   
    def view(self):  # instance method 
       print("i am watching titanic movie on below television")
       print("tv name ",self.brand)
       print(self.size)
       print(self.modelname)
       print(self.modelyear)
       print("=====================")
    
#object-reference = classname()
t1=TeleVision('SONY',50,'SU4KUHD',2018)
t1.view()
t2=TeleVision('Samsung',55,'SAMU4KUHD',2017)
t2.view()

print(TeleVision.__doc__)
    
    
    
    