#attendence

days_c=int(input("Number of classes held :"))
days_a=int(input("Number of classes attended :"))
perc_a=(days_a/days_c)*100
print('The percentage of classes attended :',perc_a)
if(perc_a>=75):
    print("Can attend Exam")
else:
    print("Cannot attend Exam")