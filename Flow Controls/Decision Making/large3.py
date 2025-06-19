# Largest among 3 numbers

num1=int(input("Enter a Number 1 :"))
num2=int(input("Enter a Number 2 :"))
num3=int(input("Enter a Number 3 :"))

if(num1>num2)&(num1>num3):
         print("Num 1 is Largest")
elif(num2>num1)&(num2>num3):
         print("Num 2 is Largest")
else:
    print("Num3 is Largest")