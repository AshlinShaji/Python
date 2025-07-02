#loc count

f=open('C:/Users/ashli/Downloads/customer1.txt','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[5]
    if loc not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1
for k,v in dic.items():
    print(k,":",v)