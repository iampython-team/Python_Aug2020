
# liril - liril 
# malayam 

text=input("Enter the string value :")

def checkPalindrome(string):
    #reverse_string=string[::-1]  # logic 1 
    reverse_string=''.join(reversed(string))  # logic 2 
    return string == reverse_string

flag=checkPalindrome(text)

if flag:
    print("this is palindorme")
else:
    print('this is not palindorme')

