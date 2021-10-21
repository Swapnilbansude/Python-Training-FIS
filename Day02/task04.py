# Write a program to compare list objects

List1 = [1,2,3,4,5,6,7]
List2 = [2,3,1,5,4,3,7]

List1.sort()
List2.sort()

if List1 == List2:
    print("List1 and List2 are equal")
elif List1 > List2:
    print("List1 is greater than List2")
elif List2 > List1:
    print("List2 is greater than List1")
else:
    print("Both lists are not equal")