
#word count problem
#to check how many words in a sentance or a paragraph

#line='cat dog mango rat cat cat dog bag mango rat rat bat'

#first of all wee need to convert this to word by word data
#for this we use split()


#cat 3
#DOG 2
#mango 2
#rat 3
#bag 1


line='cat dog mango rat cat cat dog bag mango rat rat bat'
data=line.split(' ') # after using split function it goes to a list
print(data)
dic={}
for  i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

