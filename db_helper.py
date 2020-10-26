import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword123"
)

def checkAdminId(adminId):
    mycurser = mydb.cursor()
    sqlStatement = "select * from myproject.admin where admin_id = {}".format(adminId)
    print(sqlStatement)
    mycurser.execute(sqlStatement)
    myresult = mycurser.fetchall()
    if not myresult:
        return "False"
    else:
        return myresult[0][1]


def checkAdminPassword(adminId, adminPassword):
    mycurser = mydb.cursor()
    sqlStatement = "select * from myproject.admin where admin_id = {0} and admin_password = '{1}'".format(adminId, adminPassword)
    print(sqlStatement)
    mycurser.execute(sqlStatement)
    myresult = mycurser.fetchall()
    if not myresult:
        return "False"
    else:
        # A list
        #print(myresult)

        # A Tuple
        #print(myresult[0])
        return myresult[0][1]

def getStudentDetails(stdentId):
    mycurser = mydb.cursor()
    sqlStatement = "select * from myproject.student where student_id = {}".format(stdentId)
    mycurser.execute(sqlStatement)
    myresult = mycurser.fetchall()
    if not myresult:
        return "False"
    else:
        return myresult[0]


def addStudentDetails(studentDetails):
    mycurser = mydb.cursor()

    student_id = studentDetails[0]
    roll_number = studentDetails[1]
    name = studentDetails[2]
    className = studentDetails[3]
    phone = studentDetails[4]
    address = studentDetails[5]

    sqlStatement = "INSERT INTO myproject.student VALUE ({0}, {1}, '{2}', '{3}', {4}, '{5}' )".format(student_id, roll_number, name, className, phone, address)
    print(sqlStatement)
    mycurser.execute(sqlStatement)
    mydb.commit()
    print(mycurser.rowcount, "record inserted.")

def deleteStudent(studentId):
    mycurser = mydb.cursor()
    sqlStatement = "delete from myproject.student where student_id = {}".format(studentId)
    print(sqlStatement)
    mycurser.execute(sqlStatement)
    mydb.commit()
    print(mycurser.rowcount, "record(s) deleted")

def allStudents():
    mycurser = mydb.cursor()
    sqlStatement = "select * from myproject.student"
    mycurser.execute(sqlStatement)
    myresult = mycurser.fetchall()
    return myresult