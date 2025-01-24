#note that this color: "#1581B4" is the light blue use in the app
#while this color: "#EDF7F7" is the dark blue used in the app



from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("QuizLark App")

def loginCommand():
    newWindow = Toplevel(root)



#open the image and convert it to tkinter format
backgroundImage = Image.open("images/background image.jpg")
tk_image = ImageTk.PhotoImage(backgroundImage)

#place the background image on the page
backgroundLabel = Label(root, bg= "#EDF7F7")
backgroundLabel.place(x=0, y=0, relwidth=1, relheight= 1)

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0, weight=1)

#extra space on top
spaceLabel = Label(root).pack(pady=40)



#company name
welcomeLabel = Label(root, text= "welcome", fg= "#1581B4", bg = "#EDF7F7",
font=("Montserrat Extrabold",18, "bold"), pady=1).pack(pady=0)
brandName = Label(root, text= "QuizLark", fg= "black", bg = "#EDF7F7", 
font=("Montserrat Extrabold",36, "bold" ), pady=1).pack(pady=0)

#create the buttons container
myButtons = Label(root, bg = "#EDF7F7")
myButtons.place(relx=0.5, rely=0.5,  anchor= CENTER)

#creating the buttons
playAsGuest = Button(myButtons, text="Play As Guest", fg = "white", bg="#1581B4", 
font=("Montserrat Extrabold", 16, "bold"), padx=30, pady=3)

createAccount = Button(myButtons, text="Create Account", fg="white", bg = "#1581B4", 
font=("Montserrat Extrabold", 16, "bold"), padx=30, pady=3)

login = Button(myButtons, text="Log In", fg="white", bg = "#1581B4",
font=("Montserrat Extrabold", 16, "bold"), padx=30, pady=3)

#placing the buttons on the page
playAsGuest.grid(row = 0, column = 1, pady=3, padx=3)
createAccount.grid(row= 0, column=2, pady=3, padx=20)
login.grid(row=0, column = 3, pady=3, padx=3)

#start mainloop
root.mainloop()

