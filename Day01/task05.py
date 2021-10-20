#Write a program for the following requirement
#input: a5b2c1d3
#output: aaaaabbcddd

s1 = input("Enter the string : ")
result = ""

for i in s1:
    if i.isalpha():
        temp = i
    elif i.isdigit():
        #print(temp * int(i))
        result += (temp * int(i))

print(result)
        