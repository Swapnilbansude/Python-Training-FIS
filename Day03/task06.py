#Password protection

n = int(input("Enter the total no. of plots : "))
plots = []

if n <= 0 or n > 20:
    print("Invalid input")
    exit() 

print("Enter the numbers of each plot:")
for i in range(n):
    no = int(input())
    if no <= 0:
        print("Invalid input")
        exit()
    
    plots.append(no)

#To calculate sum of even and odd numbers

listOfEven = [x for x in plots if x % 2==0]
listOfOdd = [x for x in plots if x % 2!=0]

sumOfEven = 0
for i in listOfEven:
    sumOfEven += i

sumOfOdd = 0
for i in listOfOdd:
    sumOfOdd += i

print(sumOfEven," ",sumOfOdd)
print(plots)

password = float((sumOfEven + sumOfOdd) / 2)
print("The password for the file is: {}".format(password))