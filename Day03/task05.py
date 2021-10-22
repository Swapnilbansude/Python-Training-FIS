#AEIMA's Online courses

noOfCourses = int(input("Enter the no of courses : "))
if noOfCourses < 1:
    print("Invalid no of courses")
    exit()

report = {}

for i in range(noOfCourses):
    print("Enter the name of subject and marks respectively : ")
    name = input()
    marks = int(input())
    if marks <= 0 or marks > 100:
        print("Invalid marks")
        exit()
    
    report[name]=marks

print(report)

print("The courses you have cleared are:")

for i in report.keys():
    if report[i] >= 80:
        print(i," ",report[i])
