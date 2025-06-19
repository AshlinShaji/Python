employee=["Neethu", "Anu" , "Vipin" ,"Vinay", "Rahul"]
print("Our lis is :",employee)

#using insert function
employee.insert(0,"Teena")
print(employee)

#using append() function
employee.append("Sooraj")
print(employee)

#using extend() method
employee.extend(["Albin","Helta","Arya"])
print(employee)

#del keyword
#del employee[0]
del employee[0:3]

print(employee)

employee.remove("Sooraj")
print(employee)

employee.clear()
print(employee)

del employee
print(employee)