from tkinter import *
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import re


#login frame creation

accountFrame = Frame(root, bg="#EDF7F7")
accountFormContainer = Label(accountFrame, bg="white", width=450, height=500)
accountFormContainer.grid(row=0, column=1,  anchor=E)

#create account greeting
greetingContainer = Label(accountFrame,bg="blue", width= 450, height=500)
greetingContainer.grid(row=0, column= 1, anchor=W)

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
usernameEntry.pack(anchor = W, padx=40, pady=10)

#extra space in between
Label(accountFormContainer, bg="white").pack(pady=10)

#username label and entry
usernameLabel= Label(accountFormContainer, text="username", font= ("Montserrat", 14), bg="white").pack(anchor=W, padx=40)
usernameEntry = Entry(accountFormContainer, width= 30,  bg="#EDF7F7",
 font=("Montserrat, 14"))
usernameEntry.pack(anchor = W, padx=40, pady=10)

#password label and entry
passwordLabel= Label(accountFormContainerContainer, text="password", font= ("Montserrat", 14), bg="white").pack(anchor=W, padx=40)
passwordEntry = Entry(accountFormContainer, width= 30,  bg="#EDF7F7",
 font=("Montserrat, 14"))
passwordEntry.pack(anchor = W, padx=40, pady=10)



#extra space in between
Label(formContainer, bg="white" ).pack(pady=4)

#login button
loginButton = Button(formContainer, text="Create Account", bg="#1581B4", pady=8, width=23,  
fg="white", font=("Montserrat", 16, "bold"), command = onLogin).pack( pady=10, padx=40)

#extra space in between
Label(formContainer, bg="white" ).pack(pady=5)
