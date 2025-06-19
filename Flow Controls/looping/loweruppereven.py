# #lower upper even
#
# lower=int(input("Enter the lower limit"))
# upper=int(input("Enter the upper limit"))
# i=lower
# if(i%2==0):
#     # print(i)
#     while(i<=upper):
#         print(i)
#         i=i+2
#
# else:
#     i=i+1
#     # print(i)
#     while (i <=upper):
#         print(i)
#         i = i + 2
#
#


lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
while(lower<=upper):
    if(lower%2==0):
        print(lower)
    lower+=1