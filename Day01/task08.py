#Write a program to sort the characters of a string
#input: A4J58EW2G
#output: AEGJW2458

s1 = input("Enter the string : ")
temp1 = ''
temp2 = ''

for i in s1:
    if i.isalpha():
        temp1 += i
    elif i.isdigit():
        temp2 += i

# print(temp1)
# print(temp2)  

# print(sorted(temp1))
# print(sorted(temp2))

r1 = ''.join(sorted(temp1))
#print(r1)
r2 = ''.join(sorted(temp2))
#print(r2)

print(r1+r2)