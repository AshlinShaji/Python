f=open('numbers','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))
print(lst)
print(sum(lst))

#output- ['100\n', '101\n', '102\n', '103\n', '104\n', '105\n', '106\n', '107\n', '108\n', '109\n', '110']

#rstrip()  is used to remove \n

