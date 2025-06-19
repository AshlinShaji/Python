#4 subject marks
sub1=int(input("Enter the 1st sub :"))
sub2=int(input("Enter the 2nd sub :"))
sub3=int(input("Enter the 3rd sub :"))
sub4=int(input("Enter the 4th sub :"))

total=sub1+sub2+sub3+sub4
print("Total Mark is ",total)

if(total>180):
    print("The grade is A+")
elif(total>=160)&(total<=179):
    print("The grade is A")
elif(total>=140)&(total<=159):
    print("The grade is B+")
elif(total>=120)&(total<=139):
    print("The grade is B")
elif(total>=100)&(total<=119):
    print("The grade is C+")
else:
    print("Failed")

