# Write a program for rhythm composer

# def find_prime(startNo, endNo):
#     primeNos = set()
#     for num in range(startNo, endNo+1):
#         #if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#                 else:
#                     primeNos.add(num)

#     return primeNos

def find_prime(start, end):
    result = []
    for i in range(start, end+1):

        if(i == 1 or i == 0):
            continue

        flag = 1
        for j in range(2, (i//2)+1, 1):
            if (i % j == 0):
                flag = 0
                break
        
        if flag == 1:
            result.append(i)

    return result

#print(sorted(find_prime(1,10)))



start = int(input("Enter start no : "))
end = int(input("Enter end no : "))
result = []

if start < 0 or end < 0:
    print("Invalid range")
elif start == end:
    print("There is no prime numbers in this range")
elif start > end:
    print("Invalid range (start should be less than end)")
else:
    result = sorted(find_prime(start, end))
    if result:
        print(result)
    else:
        print("There is no prime numbers in this range")


