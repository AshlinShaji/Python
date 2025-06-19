#calculate the bonus of the employee

salary=int(input("Enter the salary :"))
service=int(input("Enter the year of experience :"))
if(service>=5):
    bonus = salary * (5 / 100)
    print("The bonus is ",bonus)
else:
    print("No Bonus for the employee")