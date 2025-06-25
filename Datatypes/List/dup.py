#duplicate remove frm list

lst=[10,10,50,80,70,60,50,40,40,30,10,100]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)
