num1=int(input("Enter the 1st num :"))
num2=int(input("Enter the 2nd num :"))
num3=int(input("Enter the 3rd num :"))

if(num1>num2) and (num1>num3):
    print("Num1 is largest")
elif(num2>num1) and (num2>num3):
    print("Num2 is largest")
else:
    print("Num3 is largest")