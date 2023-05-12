pass1=input("Enter password: ")
pass2=input("Confirm password: ")
if len(pass1) >= 8:
    if pass1 == pass2:
        print("[!] Password saved.")
    else:
        print("[!] Password does not match.")
else:
    print("[!] Password length is not strong. Required 8.")