import re

def validation():
    pass_regex = '^(?=\S{12,10000}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])'
    compiled_regex = re.compile(pass_regex)
    while True:
        password1 = input("Enter a password: ")
        password2 = input("Re-enter your password: ")
        if (re.search(compiled_regex, password1)):
            if password1 == password2:
                print("Password is valid!")
                break
            else:
                print("Password do not match. Please try again!")
        else:
            print("Password does not meet the requirements. Please try again.")
                   
validation()
