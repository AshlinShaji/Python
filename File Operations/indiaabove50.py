# work in India and age above 50

f=open('C:/Users/ashli/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    loc=data[5]
    if age>'50' and loc=='india':
        print(data[1:4])