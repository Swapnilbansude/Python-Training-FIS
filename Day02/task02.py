# Write a program to remove duplicate elements from list

List = [1,2,3,1,2,3,3,3,4,4,5,6]

#1) First way

res = []
[res.append(i) for i in List if i not in res]
    
print(res)