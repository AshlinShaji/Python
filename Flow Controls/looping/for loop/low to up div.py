lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
for i in range(lower,upper+1):
    if(i%5==0):
        print(i)
