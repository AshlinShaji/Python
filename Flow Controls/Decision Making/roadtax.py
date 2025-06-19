#calculate road tax

price=int(input("Enter the price : "))

if(price>100000):
    tax1=price*(15/100)
    print("The tax amount is ",tax1)
elif(price>=50000)&(price<=100000):
    tax2=price * (10 / 100)
    print("The tax amount is ", tax2)
else:
    tax3=price * (5 / 100)
    print("The tax amount is ", tax3)
