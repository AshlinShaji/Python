f=open('fruits','r')
k=open('apfruits','w')
for i in f:
    if "apple" not in i:
        k.write(i)
