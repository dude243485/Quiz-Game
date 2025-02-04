from tkinter import *
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import re
from tkinter import messagebox
from bonus import activateGift
from store import storeCreator


#defining main window for the main menu


def menuFunction(root):
    global gift
    global money
    global xpImage
    global imageList

    def terminate():
        root.destroy()

    def giftCommand():
        activateGift(root)

    

    #Main menu page
    mainMenuFrame = Frame(root, bg="#EDF7F7")
    mainMenuFrame.place(x=0, y=0, relwidth=1, relheight= 1)
        
    

    statusContain = Label(mainMenuFrame, bg="#EDF7F7")
    statusContain.pack(fill ="x", padx= 15, pady=15 )

    #status bar
    statusBar = Label(statusContain, bg ="#EDF7F7")
    statusBar.pack(side="left")

    #image processing
    xpImage = Image.open("images/xp.png")
    money = Image.open("images/money.png")
    gift = Image.open("images/gift.png")
    store = Image.open("images/store.png")

    images = [xpImage, money, gift, store] 
    imageList =[]

    #setting image height
    for i in images:
        myHeight = 40
        aspectRatio = i.width/i.height
        newWidth = int(myHeight * aspectRatio)

        resized = i.resize((newWidth, myHeight))
        tk_image = ImageTk.PhotoImage(resized)
        imageList.append(tk_image)


    #xp widget programming
    xpValue = 250000

    xpContainer = Label(statusBar,
    bg="#EDF7F7" )
    xp = Label(xpContainer,
    image = imageList[0],
    bg ="#EDF7F7")

    xp.grid(row = 0, column= 1)

    xpAmount = Label(xpContainer, 
    text= str(xpValue),
    bg="#EDF7F7",
    font=("Montserrat", 14),
    fg="#1581B4" )
    xpAmount.grid(row=0, column=2)
    xpContainer.grid(row=0, column=0, padx=15)

    #money widget programming
    moneyValue = 5318008
    moneyContainer = Label(statusBar, bg="#EDF7F7")
    moneyContainer.grid(row=0, column=2 )

    money = Label(statusBar,
    image = imageList[1],
    bg ="#EDF7F7")
    money.grid(row=0, column= 1)

    moneyAmount = Label(moneyContainer,
    text= str(moneyValue),
    bg="#EDF7F7", 
    font= ("Montserrat", 14),
    fg="#1581B4" )
    moneyAmount.grid(row=0, column=1)


    #gift stuff
    giftContain = Label(statusContain, bg = "#EDF7F7")
    giftContain.pack(side="right", padx=20)

    giftButton = Button(giftContain,
    text= "Gift",
    bg="#EDF7F7",
    image=imageList[2],
    command=giftCommand,
    relief="flat",
    borderwidth=0
    )
    giftButton.pack()

    gift = Label(giftContain,
    text="GIFTS",
    bg ="#EDF7F7",
    fg="black",
    font=("Montserrat", 12, "bold"))
    gift.pack()


    storeContain = Label(statusContain, bg = "#EDF7F7")
    storeContain.pack(side="right", padx=20)

    storeButton = Button(storeContain,
    text= "store",
    bg="#EDF7F7",
    image=imageList[3],
    relief="flat",
    borderwidth=0
    )
    storeButton.pack()

    gift = Label(storeContain,
    text="STORE",
    bg ="#EDF7F7",
    fg="black",
    font=("Montserrat", 12, "bold"))
    gift.pack()


    #center stuff
    centerContainer = Frame(mainMenuFrame,
    bg="#EDF7F7",
    width=200,
    height=200)
    centerContainer.place(relx=0.5, rely=0.5, anchor="center")


    Label(centerContainer,
    bg="#EDF7F7",
    text="QuizLark", 
    font = ("Montserrat Extrabold", 24),
    fg = "black",
    width=20 ).pack()


    #play button 
    playButton = Button(centerContainer,
    bg="#1581B4",
    fg = "white",
    font= ("Montserrat Extrabold", 26 ),
    text= "PLAY",
    width=20)
    playButton.pack(pady=12)

    #categories button 
    categoriesButton = Button(centerContainer,
    bg="#1581B4",
    fg = "white",
    font= ("Montserrat Extrabold", 26 ),
    text= "CATEGORIES",
    width=20)
    categoriesButton.pack(pady=12)

    #stats button 
    statsButton = Button(centerContainer,
    bg="#1581B4",
    fg = "white",
    font= ("Montserrat Extrabold", 26 ),
    text= "STATS",
    width=20)
    statsButton.pack(pady=12)

    #quit button 
    quitButton = Button(centerContainer,
    bg="#1581B4",
    fg = "white",
    font= ("Montserrat Extrabold", 26 ),
    text= "QUIT",
    width=20,
    command = terminate)
    quitButton.pack(pady=12)

    return mainMenuFrame,storeButton

