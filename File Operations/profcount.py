#prof count

f=open('C:/Users/ashli/Downloads/customer1.txt','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
for k,v in dic.items():
    print(k,":",v)
