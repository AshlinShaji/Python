lst=[[101,'vinay','k',29,'bigdata',1500],
     [102,'arjun','p',27,'python',1250],
     [103,'amal','a',30,'python',1350],
     [104,'vipin','u',31,'bigdata',1600],
     [105,'naveen','g',30,'bigdata',1750],
     [106,'vineet','r',30,'python',1350]]

# bigdata prof,fname,lname,age

sum=0
for i in lst:
    sum=sum+i[5]

print(sum)