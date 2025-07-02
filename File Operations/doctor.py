#Doctor work fname,lname,age

f=open('C:/Users/ashli/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    prof=data[4]
    if prof=='Doctor':
        print(data[1:4])