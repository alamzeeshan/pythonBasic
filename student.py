import db_helper

def viewStudent():
    print("Enter Student ID")
    studentId = input()
    studentDetails = db_helper.getStudentDetails(studentId)

    if("False" == studentDetails):
        print("No such student exists")
    else:
        print(studentDetails)


def addStudent():
    print("Enter Student details seperated by '|' symbol")
    print("Example student_id | roll_number | name | class | phone | address")
    studentDetailsInput=input()
    studentDetails = studentDetailsInput.split('|')
    size = len(studentDetails)
    if(size != 6):
        print("Missing data. Please enter correct student information")
        return

    print("You entered : ")
    print(studentDetails)
    db_helper.addStudentDetails(studentDetails)

def deleteStudent():
    print("Enter student ID")
    studentId=input()
    print("You entered student ID : {}".format(studentId))
    db_helper.deleteStudent(studentId)

def allStudents():
    myresult = db_helper.allStudents()
    if not myresult:
        return "Nothing found"
    else:
        for student in myresult:
            print(student)

