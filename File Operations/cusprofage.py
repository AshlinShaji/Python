f=open('C:/Users/ashli/Downloads/customer1.txt','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    age = data[3]
    prof = data[4]
    if prof not in dic:
        dic[prof]=age
    else:
        old=dic[prof]
        if age>old:
            dic[prof]=age
for k,v in dic.items():
    print(k,":",v)