adminPassw = '111'
studentPassw = '222'
def userLogIn(userLog, userPass):
    if (userLog.lower() == 'admin') and (userPass == adminPassw):
        print("Welcome, admin")
    elif (userLog.lower() == 'student') and (userPass == studentPassw):
        print("Welcome, student")
    else:
        print("Wrong data")
def changePass(userLog, userPass):
    global adminPassw
    global studentPassw
    if (userLog.lower() == 'admin') and (userPass == adminPassw):
        adminPassw = input("Input new password for admin:")
    elif (userLog.lower() == 'student') and (userPass == studentPassw):
        studentPassw = input("Input new password for student:")
    else:
        print("Wrong data")
def userAction(login, passw, action):
    return action(login, passw)
userL = input("Login:")
userP = input("Password:")
userAnsw = input("1: LogIn; 2: Change password ")
if userAnsw == '1':
    userAction(userL, userP, userLogIn)
elif userAnsw == '2':
    userAction(userL, userP, changePass)
else:
    print("Wrong data")