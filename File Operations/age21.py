#age equal to 21 fname,lname,age,phon

f=open('C:/Users/ashli/Downloads/sample4.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    age=data[3]
    if age=='21':
        print(data[1:5])