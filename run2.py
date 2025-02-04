from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from openpyxl import load_workbook
from openpyxl import Workbook 
from categories import categoriespage
from PIL import Image, ImageTk
from tkinter import PhotoImage

def onbutton():
    cate=categoriespage(root)
    cate.place(x=0,y=0,relwidth=1,relheight=1)
    cate.tkraise()
root=Tk()
root.title("demo page")
button=Button(root,text="click me!",command=onbutton)
button.pack()
root.mainloop()