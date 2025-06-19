#Variable Length Argument

def employee(name,*skills):
    print("-----Employee Details-----")
    print("Name = ",name)
    print("Skills = ",skills)

employee("Neethu","Python")
employee("Vinay","Python","HTML,","CSS")