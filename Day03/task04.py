#Arrange Names

n = int(input("Enter the no of names : "))
names = {}

if n <= 0:
    exit()
else:
    print("Enter {} names :".format(n))
    for i in range(n):
        temp = input()
        names[temp]=len(temp)

    print(names)



