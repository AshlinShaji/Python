# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(1,6):#1  2  3
    for j in range(i,0,-1):#1  2 1  3 2 1
        print(j,end=' ')
    print()