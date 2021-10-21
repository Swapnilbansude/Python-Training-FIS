# Write a program to find max length of list and minimum element of list

List = [1,2,3,4,5]
#print(List.index(2))

# for i in List:
#     print(i)

print(max(List))
print(min(List))

nestedList = [[1,2],[3],[4,5],[6],[7,8,9]]

#To find the max length of list
maxLength = 0
for i in nestedList:
    if len(i) > maxLength:
        maxLength = len(i)

print("Maximum Length is {}".format(maxLength)) 

#To find the min length of list
minLength = 9999
for i in nestedList:
    if len(i) < minLength:
        minLength = len(i)

print("Minimum Length is {}".format(minLength))

#To find the maximum element from nested list
maxElement = 0;
for i in nestedList:
    for j in i:
        if j > maxElement:
            maxElement = j
        #print(type(j))
print("Maximum element is {}".format(maxElement))

#To find the minimum element from nested list
minElement = 9999;
for i in nestedList:
    for j in i:
        if j < minElement:
            minElement = j
        #print(type(j))
print("Minimum element is {}".format(minElement))

