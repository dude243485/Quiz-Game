#note that this color: "#1581B4" is the light blue use in the app
#while this color: "#EDF7F7" is the dark blue used in the app



from tkinter import *
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import re



root = Tk()
root.title("QuizLark App")

#*****************************************************************************************************************************
#welcome page functions


#this function changes the welcome page to the login page
#by destorying frames
def loginCommand():
    #globalize variables to allow outside access
    global loginFrame
    global welcomeFrame

    #close welcome frame
    loginFrame.tkraise()
    
    #displaying the current login frame
    loginFrame.place(x=0, y=0, relwidth=1, relheight= 1)



def accountCommand():
    global accountFrame

    #raise the account frame
    accountFrame.tkraise()
    accountFrame.place(x=0, y=0, relwidth=1, relheight=1)

#this is the frame that holds everything on our welcome page
welcomeFrame = Frame(root, bg="#EDF7F7")
welcomeFrame.place(x=0, y=0, relwidth=1, relheight= 1)


#open the image and convert it to tkinter format
backgroundImage = Image.open("images/background image.jpg")
tk_image = ImageTk.PhotoImage(backgroundImage)

#place the background image on the page
#backgroundLabel = Label(root, bg= "#EDF7F7")
#backgroundLabel.place(x=0, y=0, relwidth=1, relheight= 1)

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0, weight=1)

#extra space on top
spaceLabel = Label(welcomeFrame).pack(pady=40)



#company name
welcomeLabel = Label(welcomeFrame, text= "welcome", fg= "#1581B4", bg = "#EDF7F7",
font=("Montserrat Extrabold",18, "bold"), pady=1).pack(pady=0)
brandName = Label(welcomeFrame, text= "QuizLark", fg= "black", bg = "#EDF7F7", 
font=("Montserrat Extrabold",36, "bold" ), pady=1).pack(pady=0)

#create the buttons container
myButtons = Label(welcomeFrame, bg = "#EDF7F7")
myButtons.place(relx=0.5, rely=0.5,  anchor= CENTER)

#creating the buttons
playAsGuest = Button(myButtons, text="Play As Guest", fg = "white", bg="#1581B4", 
font=("Montserrat Extrabold", 16, "bold"), padx=30, pady=3)

createAccount = Button(myButtons, text="Create Account", fg="white", bg = "#1581B4", 
font=("Montserrat Extrabold", 16, "bold"), padx=30, pady=3, command = accountCommand)

login = Button(myButtons, text="Log In", fg="white", bg = "#1581B4",
font=("Montserrat Extrabold", 16, "bold"), padx=30, pady=3, command= loginCommand)

#placing the buttons on the page
playAsGuest.grid(row = 0, column = 1, pady=3, padx=3)
createAccount.grid(row= 0, column=2, pady=3, padx=20)
login.grid(row=0, column = 3, pady=3, padx=3)


#******************************************************************************************************************************
#login page
#regex password creation [A-Za-z0-9@#!%+=]
def checkPasswordStrength(s):
    upperCase = bool(re.search(r'[A-Z]', s))
    lowerCase = bool(re.search(r'[a-z]', s))
    digits = bool(re.search(r"\d", s))
    special = bool(re.search(r"[^A-Za-z0-9]", s))

    if upperCase and lowerCase and digits and special:
        return True

    return False

#to check if users password is in password database
def checkCorrectPassword(s):
    workbook = load_workbook("users database.xlsx")
    sheet = workbook["Sheet1"]
    #loop through each row in the password column
    for cell in sheet["B"]:
        if s == cell.value:
            return True
        
    return False

#to check if user's username is in the username database
def checkUsername(n):
    workbook = load_workbook("users database.xlsx")
    sheet = workbook["Sheet1"]
    #loop through each row in the username column
    for cell in sheet["A"]:
        if n == cell.value:
            return True

    return False


#check if username and password match
def checkCorrectDetails(s,n):
    workbook = load_workbook("users database.xlsx")
    sheet = workbook.active

    userNameRowNumber = None
    #iterating through each cell to look for current password
    for row in sheet.iter_rows(min_row=1, max_row = sheet.max_row, min_col=1, max_col = sheet.max_column):
        #looking through each row
        for cell in row:
            if cell.value == n:
                userNameRowNumber = cell.row
                break
        #if this variable has been assigned a value then break
        if userNameRowNumber:
            break
    
    #for password row number
    passwordRowNumber = None
    for row in sheet.iter_rows(min_row=1, max_row = sheet.max_row, min_col=1, max_col = sheet.max_column):
        for cell in row:
            if cell.value == n:
                passwordRowNumber = cell.row
                break
        #if this variable has been assigned a value then break
        if passwordRowNumber:
            break

    #finally check is the password and username have the same row number
    if passwordRowNumber == userNameRowNumber:
        return True

    return False


    

#login button clicked function
def onLogin():

    #globalize and store entered password
    global password
    password = passwordEntry.get()
    username = usernameEntry.get()

    #if correct password load mainmenu page
    if checkUsername(username) and checkCorrectPassword(password):
        if checkCorrectDetails(password, username):
            print("mainMenu Accessed")

    else:
        print("Password or username is incorrect")

            

    


#login frame creation
loginFrame = Frame(root, bg="#EDF7F7")
formContainer = Label(loginFrame, bg="white", width=450, height=500)
formContainer.place(relx=0.5, rely=0.5,  anchor= CENTER)

#extra space on top
Label(formContainer, bg="white").pack(pady=10)

#company name
loginBrandName = Label(formContainer, text= "QuizLark", fg= "#1581B4", bg = "white",
font=("Montserrat Extrabold",24, "bold"), pady=1).pack(pady=0)
brandName = Label(formContainer, text= "Login to your account", fg= "black", bg = "white", 
font=("Montserrat Extrabold",16, "bold" ), pady=1).pack(pady=0)

#extra space in between
Label(formContainer, bg="white").pack(pady=10)

#username label and entry
usernameLabel= Label(formContainer, text="username", font= ("Montserrat", 14), bg="white").pack(anchor=W, padx=40)
usernameEntry = Entry(formContainer, width= 30,  bg="#EDF7F7",
 font=("Montserrat, 14"))
usernameEntry.pack(anchor = W, padx=40, pady=10)

#password label and entry
passwordLabel= Label(formContainer, text="password", font= ("Montserrat", 14), bg="white").pack(anchor=W, padx=40)
passwordEntry = Entry(formContainer, width= 30,  bg="#EDF7F7",
 font=("Montserrat, 14"))
passwordEntry.pack(anchor = W, padx=40, pady=10)



#extra space in between
Label(formContainer, bg="white" ).pack(pady=4)

#login button
loginButton = Button(formContainer, text="Login", bg="#1581B4", pady=8, width=23,  
fg="white", font=("Montserrat", 16, "bold"), command = onLogin).pack( pady=10, padx=40)

#extra space in between
Label(formContainer, bg="white" ).pack(pady=5)

#*******************************************************************************************************************************
#create account page

def onCreateAccount():
    return

#login frame creation

accountFrame = Frame(root, bg="#EDF7F7")
accountFormContainer = Label(accountFrame, bg="white", width=600, height=500)
accountFormContainer.pack(side="right", fill="y", padx=120, pady=120)

#create account greeting
greetingContainer = Label(accountFrame,bg="#EDF7F7", width= 450, height=500, padx=50, pady=50)
greetingContainer.pack(side="left", fill="y", pady=120, padx=110)

Label(greetingContainer, text="QuizLark", font= ("Montserrat", 36, "bold"), fg="#1581B4", bg="#EDF7F7").pack(anchor=W)
Label(greetingContainer, text="Welcome to the best quizzing app out there...", wraplength=380,
font=("Montserrat", 18, "bold"), fg="black", bg="#EDF7F7", justify="left").pack(anchor=W,padx=10)

#extra space on top
Label(accountFormContainer, bg="white").pack(pady=10)

#company name
loginBrandName = Label(accountFormContainer, text= "QuizLark", fg= "#1581B4", bg = "white",
font=("Montserrat Extrabold",24, "bold"), pady=1).pack(pady=0)
brandName = Label(accountFormContainer, text= "Login to your account", fg= "black", bg = "white", 
font=("Montserrat Extrabold",16, "bold" ), pady=1).pack(pady=0)

#extra space in between
Label(accountFormContainer, bg="white").pack(pady=10)

#username label and entry
fullnameLabel= Label(accountFormContainer, text="Fullname", font= ("Montserrat", 14), bg="white").pack(anchor=W, padx=40)
fullnameEntry = Entry(accountFormContainer, width= 30,  bg="#EDF7F7",
 font=("Montserrat, 14"))
fullnameEntry.pack(anchor = W, padx=40, pady=10)


#username label and entry
usernameLabel= Label(accountFormContainer, text="username", font= ("Montserrat", 14), bg="white").pack(anchor=W, padx=40)
usernameEntry = Entry(accountFormContainer, width= 30,  bg="#EDF7F7",
 font=("Montserrat, 14"))
usernameEntry.pack(anchor = W, padx=40, pady=10)

#password label and entry
passwordLabel= Label(accountFormContainer, text="password", font= ("Montserrat", 14), bg="white").pack(anchor=W, padx=40)
passwordEntry = Entry(accountFormContainer, width= 30,  bg="#EDF7F7",
 font=("Montserrat, 14"))
passwordEntry.pack(anchor = W, padx=40, pady=10)


#login button
createAccount = Button(accountFormContainer, text="Create Account", bg="#1581B4", pady=8, width=23,  
fg="white", font=("Montserrat", 16, "bold"), command = onCreateAccount).pack( pady=10, padx=40)

#extra space in between
Label(accountFormContainer, bg="white" ).pack(pady=5)






#start mainloop
root.mainloop()

