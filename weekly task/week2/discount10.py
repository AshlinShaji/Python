quantity=int(input("Enter the quantity :"))
cost=quantity*100
print("The cost is ",cost)
if(quantity>1000):
    dis=cost*(10/100)
    print("The cost after discount is",cost-dis)
else:
    print("The cost is ",cost)