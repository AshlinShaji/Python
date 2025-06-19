#calculator

def Addition(x,y):
    return x+y
def Diffrence(x,y):
    return x-y
def Multiplication(x,y):
    return(x*y)
def Division(x,y):
    return(x/y)

print("A.Addition")
print("B.Substraction")
print("C.Multiplication")
print("D.Division")
print()

num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
print()
choice=input("Enter your choice")

if(choice=="A")or(choice=="a"):
    print("Sum =",Addition(num1,num2))
elif(choice=="B")or(choice=="b"):
        print("Diffrence =",Diffrence(10,7))
elif(choice=="C")or(choice=="c"):
    print("Multiplication =",Multiplication(3,4))
elif(choice=="D")or(choice=="d"):
    print("Division =",Division(18,3))
else:
    print("Invalid choice")