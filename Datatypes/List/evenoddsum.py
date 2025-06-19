lst=[]
lste=[]
lsto=[]
sum=0
sume=0
sumo=0
for i in range(1,101):
    lst.append(i)
    sum=sum+i

    if(i%2==0):
        lste.append(i)
        sume=sume+i
    else:
        lsto.append(i)
        sumo=sumo+i
print(sum)
print(sume)
print(sumo)
print(sum+sume+sumo)