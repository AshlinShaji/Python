num=int(input("Enter a number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
if(flag>0):
        print("Not a prime number")
else:
        print("Prime")
