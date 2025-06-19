num1=int(input("Enter a Number 1 :"))
num2=int(input("Enter a Number 2 :"))
num3=int(input("Enter a Number 3 :"))

if((num1>num2)&(num1>num3))&((num2<num1)&(num2<num3)):
         print("Num 3 is 2nd Largest")
elif((num2>num1)&(num2>num3))&((num3<num1)&(num3>num2)):
         print("Num 1 is 2nd Largest")
else:
    print("Num2 is 2nd Largest")