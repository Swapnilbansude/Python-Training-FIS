# Reverse the order of word, get input from the keyboard

orignalString = input("Enter the string : ")

words = orignalString.split()
print(words)

reverseString = ' '.join(words[::-1])
print(reverseString)



