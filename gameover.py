
from tkinter import *
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import re
from tkinter import messagebox



gameOverMsg = Toplevel()
gameOverMsg.title("Pause")
#setting the window size

gameOverMsg.resizable(False, False)

screenWidth = gameOverMsg.winfo_screenwidth()
screenHeight = gameOverMsg.winfo_screenheight()


#centering the window
x = (screenWidth//2)-(300//2)
y = (screenHeight//2)-(220//2)
gameOverMsg.geometry(f"300x220+{x}+{y}")
gameOverMsg.configure(bg=lightBlue)

def onQuit():
    #open mainmenu
    #openMainMenu()
    gameOverMsg.destroy()


Label(gameOverMsg,bg=lightBlue).pack(pady=2)

Label(gameOverMsg,
text="Gameover",
fg="black",
bg=lightBlue,
font=("Montserrat Extrabold", 17),
justify="center").pack(pady=10)

quitButton = Button(gameOverMsg,
text="QUIT",
bg=darkBlue,
width=20,
fg="white",
command=onQuit,
font=("Montserrat", 13, "bold"),
pady=5).pack(pady=8)


#make it appear on top of current window
gameOverMsg.transient(root)

#disable the main window
gameOverMsg.grab_set()

#wait for Pause window to close
root.wait_window(gameOverMsg)