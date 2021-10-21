# Reverse the order of word, get input from the keyboard

orignalString = input("Enter the string : ")

words = orignalString.split()
print(words)
# print(words[-2])

#1) First way

# reverseString = ' '.join(words[::-1])
# print(reverseString)

#2) Second way

# reverseString = ' '.join(reversed(words))
# print(reverseString)

#3) Third way
result = ''
for s in words[::-1]:
    result += s + ' '
    # print(s)

print(result)



