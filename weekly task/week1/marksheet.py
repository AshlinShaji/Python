sub1=int(input("Enter the 1st sub :"))
sub2=int(input("Enter the 2nd sub :"))
sub3=int(input("Enter the 3rd sub :"))
sub4=int(input("Enter the 4th sub :"))
sub5=int(input("Enter the 5th sub :"))

total=sub1+sub2+sub3+sub4+sub5
print("Total Mark is ",total)
average=(total/5)
print("Average is",average)
if average >= 90:
    grade='A'
elif average >= 80:
    grade='B'
elif average >= 70:
    grade='C'
elif average >= 60:
    grade='D'
else: grade='F'
print("Average Marks:", average)
print("Grade:", grade)

