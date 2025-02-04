from tkinter import *
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import re
from tkinter import messagebox


def activateGift(root, userIndex):
    global diamondGift
    global imageList
    global images

    bonus = Toplevel(root)
    bonus.title("Gifts")

    #setting size and background color
    bonus.geometry("350x450")
    bonus.configure(bg="#EDF7F7")

    #the details about this particular gift
    giftTitle = "Save me x3"
    giftdetails = "Maintain your progress and keep playing after getting a question wrong."

    #the gift image
    eliminatePic = Image.open("images/eliminate.png")
    instantPic = Image.open("images/instant.png")
    hintPic = Image.open("images/hint.png")

    images = [eliminatePic, instantPic, hintPic] 
    imageList =[]

    #setting image height
    for i in images:
        myHeight = 160
        aspectRatio = i.width/i.height
        newWidth = int(myHeight * aspectRatio)

        resized = i.resize((newWidth, myHeight))
        tk_image = ImageTk.PhotoImage(resized)
        imageList.append(tk_image)

    #space above
    Label(bonus,
    bg="#EDF7F7").pack(pady=10)

    Label(bonus,
    text="Welcome Bonus!",
    font= ("Montserrat", 16, "bold"),
    justify= "center",
    bg="#EDF7F7",
    fg="black").pack(pady=5)

    #Gift title
    Label(bonus,
    text =  str(giftTitle),
    font= ("Montserrat", 32, "bold"),
    bg="#EDF7F7",
    fg="black"
    ).pack()

    Label(bonus, 
    bg ="#EDF7F7",
    image =imageList[0]).pack(pady=10)


    Label(bonus,
    text=str(giftdetails),
    font= ("Montserrat", 10),
    justify= "center",
    bg="#EDF7F7",
    wraplength= 260,
    fg="black").pack(pady=2)

    continueButton = Button(bonus,
    bg="#1581B4",
    fg="white",
    font=("Montserrat", 14, "bold"),
    justify="center",
    text="continue",
    width= 23,
    command=bonus.destroy).pack(pady=8)

    return bonus