
#age above 50 fname,lname,age,prof

f=open('C:/Users/ashli/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    if age>'50':
        print(data[1:5])
