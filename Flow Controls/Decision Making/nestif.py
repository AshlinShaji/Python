# if(condition1):
#     if(subcondition1):
#         statement_1
#     else:
#         statement_2
# elif(condition2):
#     if(subcondition3):
#         statemnet_3
#     else:
#         statement_4
# else:

num1=int(input("Enter a Number 1 :"))
num2=int(input("Enter a Number 2 :"))
num3=int(input("Enter a Number 3 :"))

if(num1>num2)&(num1>num3):
    if(num2>num3):
         print("Num 2 is 2nd Largest")
    else:
        print("Num3 is 2nd largest")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
         print("Num 1 is 2nd Largest")
    else:
        print("num2 is 2nd largest")
elif(num3>num1)&(num3>num2):
    if(num1>num3):
         print("Num 1 is 2nd Largest")
    else:
        print("num3 is 2nd largest")
else:
    print("Invalid")