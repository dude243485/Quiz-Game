from tkinter import *
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import re
from tkinter import messagebox


def storeCreator(root, mainMenuFrame):

    global saveMePic
    global eliminatePic
    global instantPic
    global hintPic 
    global images 
    global imageList 
    global backButton

    #your functions
    def goBack():
        mainMenuFrame.tkraise()

    #create the store frame
    storeFrame = Frame(root, bg="#EDF7F7")
    storeFrame.place(x=0, y=0, relwidth=1, relheight= 1)

    #open the image
    backButton = Image.open("images/back arrow.png")

    #define your chosen height
    backButtonHeight = 50

    #get the image aspect ratio
    backButtonRatio = backButton.width/backButton.height

    #use the aspect ratio to calculate the new width
    newWidth = int(backButtonHeight*backButtonRatio)

    #resize the image
    resized = backButton.resize((newWidth, backButtonHeight))
    backButton = ImageTk.PhotoImage(resized)

    #create your back button
    Button(storeFrame,
    image=backButton,
    command= goBack,
    bg="#EDF7F7",
    relief="flat",
    borderwidth=0).pack(
        side="top",
        anchor="nw",
        pady=15,
        padx=30
    )

    #creating your header
    Label(storeFrame, 
    text="POWER-UP STORE",
    font=("Montserrat Extrabold", 36),
    fg="black",
    bg="#EDF7F7",
    justify="center"
    ).pack()

    #for the center frame
    centerFrame = Frame(storeFrame, bg="#EDF7F7")
    centerFrame.pack()

    saveMePic = Image.open("images/save me.png")
    eliminatePic = Image.open("images/eliminate.png")
    instantPic = Image.open("images/instant.png")
    hintPic = Image.open("images/hint.png")


    images = [saveMePic,eliminatePic,instantPic,hintPic] 
    imageList =[]

    saveMeQuantity = 9
    instantQuantity =25
    eliminateQuantity = 16
    hintQuantity = 12

    #setting image height
    for i in images:
        myHeight = 160
        aspectRatio = i.width/i.height
        newWidth = int(myHeight * aspectRatio)

        resized = i.resize((newWidth, myHeight))
        tk_image = ImageTk.PhotoImage(resized)
        imageList.append(tk_image)


    def itemcreator(container, itemName,itemDetails,itemImage, itemQuantity):
        #for item name
        this = Label(container, bg= "white")
        this.pack(side="left",  padx=15)

        #space below
        Label(this, bg= "white").pack(pady=3)

        Label(this,
        text= itemName,
        font= ("Montserrat Extrabold", 24),
        justify= "center",
        bg="white",
        fg="black").pack(pady=5)

        Label(this,
        text=str(itemDetails),
        font= ("Montserrat", 10),
        justify= "center",
        bg="white",
        wraplength= 230,
        fg="black").pack(pady=2)

        #Gift title
        Label(this,
        text = "In-stock: " + str(itemQuantity),
        font= ("Montserrat", 16, "bold"),
        bg="white",
        fg="#1581B4"
        ).pack()


        Label(this, 
        bg ="white",
        image = itemImage).pack(pady=10)

        
        

        buyButton = Button(this,
        bg="#1581B4",
        fg="white",
        font=("Montserrat", 14, "bold"),
        justify="center",
        text="buy",
        pady=3,
        width=18,
        ).pack(pady=8,padx=20)

        #space below
        Label(this, bg= "white").pack(pady=2)


    #defining the save me label
    saveMe = itemcreator(centerFrame,
    "SAVE ME",
    "Maintain your progress and keep playing after getting a question wrong.",
    imageList[0],
    str(saveMeQuantity )
    )

    #instant Label
    instant = itemcreator(centerFrame,
    "INSTANT",
    "Provides the correct answer to the current question.",
    imageList[2],
    str(instantQuantity )
    )

    #eliminate Label
    eliminate = itemcreator(centerFrame,
    "ELIMINATE",
    "Eliminates two wrong answers from the current question.",
    imageList[1],
    str(eliminateQuantity )
    )

    #hint Label
    hint = itemcreator(centerFrame,
    "HINT",
    "Displays a hint on the current question.",
    imageList[3],
    str(hintQuantity )
    )


    return storeFrame