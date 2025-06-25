a, b, c, d = map(int, input("Enter IP (4 numbers): ").split())
for i in range(5):
    d += 1
    if d > 255:
        d = 0
        c += 1
        if c > 255:
            c = 0
            b += 1
            if b > 255:
                b = 0
                a += 1
    print(a, b, c, d)
