# Write a program to merge characters of two strings
#input: string1-> abcd , string2-> efgh

s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")

result = ''
diff = 0;

if len(s1) < len(s2):
    diff = len(s2) - len(s1)
    #print(diff)
    for i in range(len(s1)):
        result += s1[i] + s2[i]

    #print(i)  
    result += s2[i+1:] 

elif len(s2) < len(s1):
    diff = len(s1) - len(s2)
    #print(diff)
    for i in range(len(s2)):
        result += s2[i] + s1[i]

    #print(i)  
    result += s1[i+1:] 
else:
    for i in range(len(s2)):
        result += s1[i] + s2[i]


print(result)
    
