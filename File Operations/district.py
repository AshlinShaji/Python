f=open('C:/Users/ashli/Downloads/temper.unknown','r')
dic=()
for i in f:
    data=i.rstrip('\n').split(',')
    district=data[0]
    temper=data[1]
    if district not in dic:
        dic[district]=temper
    else:
        old=dic[district]
        if temper>old:
            dic[district]=temper
for k,v in dic.items():
    print(k,":",v)