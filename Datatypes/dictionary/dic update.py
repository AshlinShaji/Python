dic={'id':101,'name':'vinay','age':27,'prof':'bigdata','salary':1500}
print(dic)

#for updating key value
dic['age']=30
dic['prof']='python'
dic['salary']+=500
print(dic)


#For adding new key

dic['location']='Ernklm'
print(dic)

#to check values in a dictionary
print('age' in dic)
print('name' not in dic)
