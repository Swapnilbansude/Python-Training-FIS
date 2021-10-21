# Write a program to reverse the elements of tuple without using built in function


t = (10,20,30,40,50)
print(type(t))
# List = [1,2,3]
# List.reverse()
# print(t[2])

# for i in t:
#     print(i)

temp = [x for x in t[::-1]]
#print(temp)

result = tuple(temp)
print(type(result))
print(result)


