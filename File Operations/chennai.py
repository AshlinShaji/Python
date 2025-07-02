#Chennai work fname,lname,age

f=open('C:/Users/ashli/Downloads/sample4.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[5]
    if loc=='Chennai':
        print(data[1:4])