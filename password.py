'''
I, Sumit Aggarwal, student number:000793607, certify that all code submitted is
my own code, that I have not copied it from any source. I also certify that I
have not allowed anyone else to copy my code.
'''

import re

def passwordIsOk():
    
    x= True
    while x:
        pwd= input("Enter your password ")
        if len(pwd)<=0 or len(pwd)<10:
            print("Your password should have at least 10 characters")
        elif not re.search("[A-Z]",pwd):
            print("Your password should have at least one upper case letter")
        elif not re.search("[0-9]",pwd):
            print("Your password should have at least one number")
        elif not re.search("[$#%&*]",pwd):
            print("Your password should have a special character") 
        elif " " in pwd:
            print("Your password should not have any spaces")
        else:
            print("Password accepted")
            x=False
            break
    if x:
        print("Invalid password")
            

passwordIsOk()
        
    







    
