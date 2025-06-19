password=input("Enter the string to check :")

if len(password)>=8:
    if any(char.isdigit() for char in password):
        print("The Password is strong")
    else:
        print("Enter atleast one digit")
else:
    print("The password must be greater than 7 character")











