#Uk work fname,lname,age,prof

f=open('C:/Users/ashli/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[5]
    if loc=='uk':
        print(data[1:5])