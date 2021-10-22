#Write a program to get student details from user and creates a dict.
#Display students marks by taking student id as a input .
#Implement exception concept in case if the user is providing marks > 100

class MoreMarksException(Exception):
    def __init__(self, args):
        self.msg = args





print("----Enter student details----")
id = input("Enter the id : ")
name = input("Enter the name : ")
subject = input("Enter the subject : ")

marks = int(input("Enter the marks : "))
if marks > 100:
    raise MoreMarksException("Please enter valid marks")

details = {"Name": name, "Subject":subject, "Marks":marks}

students = {id:details}

print(students)

# print(students['1']["Marks"])

result = input("Enter the id of students : ")

if result in students.keys():
    print(students[result]["Marks"])
else:
    print("Student is not present with id {}".format(result))