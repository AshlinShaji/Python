num=int(input("Enter the number"))
if(num<0):
    print("Enter a positive number")
elif(num==0):
    print("You have entered zero")
elif(num==1):
    print("1 is a composite number")
else:
    for i in range(2,num):
        if num%i==0:
            print(num," is not a prime number")
            break

    print("Number is prime")
