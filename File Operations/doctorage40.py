#Doctor and age>40 work fname,lname,age

f=open('C:/Users/ashli/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    prof=data[4]
    age=data[3]
    if prof=='Doctor' and age>'40':
        print(data[1:4])