
    
def upper_decarator(function):
    def inner():
        new_greetings=function().upper()
        print(new_greetings)  
    return inner()

@upper_decarator #=upper_decarator(show)
def show():
    str="hello! Good Morning"
    print(str)
    return str

@upper_decarator #=upper_decarator(show)
def show2():
    str="ciao .... italian"
    print(str)
    return str

#upper_decarator(show)

#upper_decarator(show2())


