sub1=int(input("Enter the 1st sub :"))
sub2=int(input("Enter the 2nd sub :"))
sub3=int(input("Enter the 3rd sub :"))
sub4=int(input("Enter the 4th sub :"))

total=sub1+sub2+sub3+sub4
print("Total Mark is ",total)

if(total<25):
    print("The grade is F")
elif(total>=25)&(total<=45):
    print("The grade is E")
elif(total>=45)&(total<=50):
    print("The grade is D")
elif(total>=50)&(total<=60):
    print("The grade is C")
elif(total>=60)&(total<=80):
    print("The grade is B")
else:
    print("The grade is A")

