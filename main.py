import db_helper
import student

def start():
    print("Welcome Admin, please enter your id")
    adminId = input()   
    adminName = db_helper.checkAdminId(adminId) 
    if adminName == "False":
        print("No such admin exists")
        return
    
    print("Please enter password for admin {}".format(adminName))
    adminPassword = input()
    pwdResult = db_helper.checkAdminPassword(adminId, adminPassword)
    if pwdResult == "False":
        print('Invalid passord for user {}'.format(adminName))
        return
    
    print("Welcome {}".format(adminName))
    studentOperations()

    


def studentOperations():
    print("\n\nPlease select your options")
    print("1. To view Student")
    print("2. Add Student")
    print("3. Delete Student")
    print("4. View All Student")
    print("5. Exit\n\n")

    option = input()

    if (option == '5'):
        return

    if (option == '1'):
        student.viewStudent()
    elif (option == '2'):
        student.addStudent()
    elif (option == '3'):
        student.deleteStudent()
    elif (option == '4'):
        student.allStudents()
    else:
        print("Invalid option. Please try again")
        
    studentOperations() 

if __name__ == "__main__":
    start()