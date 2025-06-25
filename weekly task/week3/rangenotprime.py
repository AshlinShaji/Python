start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start, end + 1):
    if i < 2:
        print(i)
    else:
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count != 0:
            print(i)
