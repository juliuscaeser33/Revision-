libraryAdminPassW=1234
StudPassW=4321
def userLogIn(userName, userPass):
    userName=input("Enter your name:")
    userLogIn=int(input("Enter your password:"))
    if (userName.lower()=="admin") and (userLogIn==libraryAdminPassW):
        print("welcome admin")
    elif (userName.lower()=="student") and (userLogIn==StudPassW):
        print(f"welcom {userLogIn}")
    else: print("invalid data")
#changing password
def changePassW(userName,userPass):
   global libraryAdminPassW
   global StudPassW
   
   if (userName.lower()=="admin") and (userLogIn==libraryAdminPassW):
       libraryAdminPassW=int(input("please enter new password"))
   elif (userName.lower()=="student") and (userLogIn==StudPassW):
       StudPassW=int(input( "please enter new passpord"))
   else: print("wrong password")
#NewlibraryPassW=0000
#NewStudentPasW=1111
#changePassW("student",)
def userAction(login, passw, action):
    return action(login, passw)
userL = input("Login:")
userP = input("Password:")
userAnsw = input("1: LogIn; 2: Change password ")
if userAnsw == '0000':
    userAction(userL, userP, userLogIn)
elif userAnsw == '1111':
    userAction(userL, userP, changePassW)
else:
    print("Wrong data")