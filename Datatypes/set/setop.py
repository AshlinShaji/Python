#Set Operations


#1.union


#2.Intersection



#3.Difference

st1={1,2,3,4,5,6,7,8,9,10}
st2={5,2,7,8,9,10,11,12,13,14,15}


#Union  - combining 2 set as one

#(1,2,3,4,5,........,15}

st3=st1.union(st2)
print(st3)

#intersection - commom element

st3=st1.intersection(st2)
print(st3)

#Diffrence

st1={1,2,3,4,5,6,7,8,9,10}
st2={5,6,7,8,9,10,11,12,13,14,15}

st3=st1.difference(st2)
print(st3)
