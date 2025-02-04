#import necessary libraries
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from openpyxl import load_workbook
from openpyxl import Workbook 
from statmain import statgenerator
from PIL import Image, ImageTk
from tkinter import PhotoImage

def onbutton():
    my_stat=statgenerator(root)
    my_stat.place(x=0,y=0,relwidth=1,relheight=1)
    my_stat.tkraise()
root=Tk()
root.title("demo page")
button=Button(root,text="click me!",command=onbutton)
button.pack()
root.mainloop()