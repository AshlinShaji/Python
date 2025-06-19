word=input("Enter the string to check :")

s=word[0]
if('A'<= s <= 'Z') or('a' <= s <= 'z')or (s=='_'):
    print("The string is a Identifier ")
else:
    print("The string is not a Identifier")



