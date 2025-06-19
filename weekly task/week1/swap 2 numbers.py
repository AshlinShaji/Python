num1=int(input("Enter the 1st num :"))
num2=int(input("Enter the 2nd num :"))

print("Before Swapping")
print("num1 is ",num1," num2 is ",num2)

num3=num1+num2
num2=num1
num1=num3-num2

print("After Swapping")
print("num1 is ",num1," num2 is ",num2)