#Age above 23 and location  chennai
#print fname,lname,age,phon


f=open('C:/Users/ashli/Downloads/sample4.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[5]
    age=data[3]
    if loc=='Chennai' and age>'23':
        print(data[1:5])