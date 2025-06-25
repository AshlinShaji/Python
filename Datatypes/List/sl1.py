#empty list 1 to 20 elemnts
#list ====>cube

lst=[]
for i in range(1,21):
    lst.append(i)
print(lst)

lst1=[]
for i in lst:
    lst1.append(i**3)
print(lst1)    