
import re

password = input("Enter your password : ")

# This function is used to verify the strength of the password
def check_password_strength(password):
        isStrongPassword = True
        if len(password) < 8:
            print("Make sure your password is at least 8 characters long")
            isStrongPassword = False
            return isStrongPassword
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a upper case letter in it")
            isStrongPassword = False
            return isStrongPassword
        elif re.search('[a-z]',password) is None: 
            print("Make sure your password has a lower case letter in it")
            isStrongPassword = False
            return isStrongPassword
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
            isStrongPassword = False
            return isStrongPassword
        elif re.search('[^a-zA-Z0-9\s]',password) is None:
            print("Make sure your password has a special character in it")
            isStrongPassword = False
            return isStrongPassword
        else:
            print("Your password is good !")
            return isStrongPassword
        

check_password_strength(password)