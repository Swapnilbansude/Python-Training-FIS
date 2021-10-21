# Write a program to display unique vowels present in the word 

#word = input("Enter word : ")
word = "simiplea"
vowels = "aeiou"
result = []

l = list(word)
#print(l)

for i in l:
    #print(i)
    if i in vowels and i not in result:
        result.append(i)

print(result)
