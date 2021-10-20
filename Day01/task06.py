#Write a program to remove integers from the given string
#input: a1bc34e3
#output: abce

s1 = input("Enter string : ")

for i in s1:
    if i.isdigit():
        s1 = s1.replace(i,'')

print(s1)