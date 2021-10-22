# Write a program to find the number of occurences of each vowel present in the given string 
#Use dictionary
#input: doganimaldoganimal
#output: a occurs 4 times, o occurs 2 times

s = "doganimaldoganimal"
print(s)

vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for i in s:
    #print(i)
    if i in vowels.keys():
        vowels[i] += 1

print(vowels)    

for key in vowels.keys():
    print("{} occurs {} times.".format(key, vowels[key]))