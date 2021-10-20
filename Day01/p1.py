#Data types and keywords

#This is used to get the keywords list in python
import keyword

print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


'''
Datatypes in python are dynamically type
We don't have to specify the type of data explicitly

Datatypes: int, float, bool, str
            complex, byte, range, tuple, list, set, dict, None
'''

#1) int
# i. decimal
a = 10
print(type(a))

# ii. binary
# binary numbers can be represented with leading 0b or 0B
b = 0b100
print(b)
print(type(b))

# iii. Octal
# octal numbers can be represented with leading 0o or 0O
c = 0o0101
print(c)
print(type(c))

# iv. Hexadecimal
# hexadecimal numbers can be represented with leading 0o or 0O
d = 0x1f0
print(d)
print(type(d))

#2) float
#3) bool
#4) complex - real and imaginary value
comp = 3 + 5j
print(type(comp))

