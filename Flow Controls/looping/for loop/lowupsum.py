lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
esum=0
osum=0
for i in range(lower,upper+1):
    if(i%2!=0):
        osum=osum+i


    else:
        esum = esum + i

print("Sum of even is",esum)
print("Sum of odd is",osum)


