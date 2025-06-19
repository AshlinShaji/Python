side1=int(input("Enter the 1st side:"))
side2=int(input("Enter the 2nd side:"))
side3=int(input("Enter the 3rd side:"))

if(side1==side2==side3):
    print("The traingle is equalateral")
elif(side1==side2)or(side1==side3)or(side2==side3):
    print("The traingle is isoscoles")
else:
    print("The traingle is scalene")