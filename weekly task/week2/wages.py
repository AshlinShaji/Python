age=int(input("Enter the age :"))
sex=input("Enter the sex  (M or F) :")
day=int(input("Enter the days worked :"))
if(age>=18)and (age<30) :
    if(sex=="M" or "m"):
        print("Wages is ",(700*day))
    elif(sex=="F" or "f"):
        print("Wage is ",750*day)
    else:
        print("Enter the valid term")
elif (age >= 30) and (age < 40):
    if (sex == "M" or "m"):
        print("Wages is ",800*day)
    elif (sex == "F" or "f"):
        print("Wage is ",850*day)
    else:
        print("Enter the valid term")
else:
    print("Enter the age below 40 ")
