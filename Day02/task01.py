#Write a program to add all items in the list

noOfItems = int(input("Enter the no of items : "))
List = []

for i in range(noOfItems):
    temp =  input("Enter the item : ")
    List.append(temp)

print(List)