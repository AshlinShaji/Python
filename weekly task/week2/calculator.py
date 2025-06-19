num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number :"))
op=input("Enter the operator :")

if(op=="+"):
    print("Your Answer is ",num1+num2)
elif(op=="-"):
    print("Your Answer is ",num1-num2)
elif(op=="*"):
    print("Your Answer is ",num1*num2)
elif(op=="/"):
    print("Your Answer is ",num1/num2)
else:
    print("Enter the valid operator")