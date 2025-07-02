f=open('golf','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(' ')
    print(data)
#     dic={}
    for  i in data:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
print(dic)

