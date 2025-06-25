num = int(input("Enter the number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
print("The sum of proper divisors is", sum)
if num == sum:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
