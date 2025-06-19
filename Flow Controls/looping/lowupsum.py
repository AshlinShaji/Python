lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
esum=0
osum=0
while(lower<=upper):
    if(lower%2!=0):
        osum=osum+lower


    else:
        esum = esum + lower

    lower += 1
print("Sum of even is",esum)
print("Sum of odd is",osum)


