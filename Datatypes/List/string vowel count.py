#vovel count

string='ashlinshaji'
lst=['a','e','i','o','u','A','E','I','O',U'']
count=0
for i in string:
    if i in lst:
        count+=1
print(count)