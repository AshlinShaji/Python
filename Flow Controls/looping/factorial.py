#factorial

num=int(input("Enter the number :"))
i=1
fac=1
while(i<=num):
    fac*=i
    i+=1
print("The factorial is",fac)