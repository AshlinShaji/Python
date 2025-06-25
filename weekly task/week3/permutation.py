data=[1,2,3]
print("The Orginal data ",data)
print("Collection of permutation")
for i in data:
    for j in data:
        for k in data:
            if i!=j and j!=k and k!=i:
                print([i,j,k])