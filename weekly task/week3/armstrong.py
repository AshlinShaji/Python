num = int(input("Enter a Number: "))
original = num
sum = 0
while num != 0:
    dig = num % 10
    sum = sum + (dig * dig * dig)
    num = num // 10
if sum == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")




