lst=[[101,'vinay','k',29,'bigdata',1500],
     [102,'arjun','p',27,'python',1250],
     [103,'amal','a',30,'python',1350],
     [104,'vipin','u',31,'bigdata',1600],
     [105,'naveen','g',30,'bigdata',1750],
     [106,'vineet','r',30,'python',1350]]

# bigdata prof and age above 29 fname,lname,age

for i in lst:
    if i[4]=='bigdata' and i[3]>29:

        print(i[1:4])