num=int(input("Enter a Number"))
org=num
sum=0
while(num!=0):
	dig=num%10
	sum=sum+(dig**3)
	num=num//10
if(sum==org):
	print("It is an armstrong")
else:
	print("It is not a Armstrong")



