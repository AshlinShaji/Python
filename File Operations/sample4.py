f=open('C:/Users/ashli/Downloads/sample4.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    if age>'23':
        print(data)
