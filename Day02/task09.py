# Write a program to find the elements in a given set that are not in another set

set1 = {10,20,30,40}
set2 = {30,40,50,60}

print(set1.intersection(set2))

#1) First
print(set1 - set2)
print(set2 - set1)

#2) Second
temp = set1.intersection(set2)
print(set1 - temp)
print(set2 - temp)