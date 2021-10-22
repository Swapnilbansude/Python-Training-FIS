'''
d = dict()
print(d)
print(type(d))

d[1]="Java"
d[2]="Python"
d[3]="C#"
d[4]="Javascript"
print(d)
'''

# l = [10,20,30,40]
# d = dict(l)
# print(d)

'''
d = {1:"One", 2:"Two", 3:"Three", 4:"Four"}
print(d)
print(d.keys())
print(d.values())

d[2]="New Two"
print(d)

d[5]="Five"
print(d)

print(d.get(2))

print(d.popitem())
'''

# def find_prime(start, end):
#     result = []
#     for i in range(start, end+1):

#         if(i == 1 or i == 0):
#             continue

#         flag = 1
#         for j in range(2, (i//2)+1, 1):
#             if (i % j == 0):
#                 flag = 0
#                 break
        
#         if flag == 1:
#             result.append(i)

#     return result

# print(find_prime(1,11))

n = int(input("Enter no of names : "))
names = []

print("Enter names : ")
for i in range(n):
    names.append(input())

names.sort(key=str.lower, reverse=True)

print(names)