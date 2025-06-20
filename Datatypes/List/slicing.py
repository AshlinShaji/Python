#list slicing

#slicing is used when we need to get the data between particular position


lst=[1,6,2,10,17,12,30,34,20,25,40,100,75]

#index
print(lst[3:6])  #3,4,5  [10,17,12]
print(lst[2:7]) #2,3,4,5,6   [2,10,17,12,30]
print(lst[4:])  #4,....  [17, 12, 30, 34, 20, 25, 40, 100, 75]
print(lst[:5]) #.....4  [1, 6, 2, 10, 17]