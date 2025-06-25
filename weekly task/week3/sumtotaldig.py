num = int(input("Enter a Number: "))
org = num
sum = 0

while num != 0:
    dig = num % 10
    sum = sum + dig
    num = num // 10

print("Sum of digits:", sum)

