#calculate electricity bill


unit=int(input("Enter the Units :"))
if(unit<=100):
    fees=0
elif(unit>=101)&(unit<=200):
    fees=(unit-100)*5
else:
     fees=(unit-200)*10+500
print("Fees is for units is ",fees)
