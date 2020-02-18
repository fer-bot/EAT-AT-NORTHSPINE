#####   HOME FRAME   ####
'''
INPUTS:
- root
- filename for background
- filename for logo (150x150) of the application
- function to jump to type frame
- function to jump to userdate
- function to jump to description
'''
## IMPORTS ##
from tkinter import *
import datetime
from tkinter.messagebox import *
from functions import*
import pickle
import global_var

## GLOBAL VARIABLES ##
currenttime = datetime.datetime.now()
menu_name=''

## FUNCTIONS ##

def home(root, filename1,filename2, jump1, jump2, jump3):
    currenttime = datetime.datetime.now()
    frame1 = Frame(root)
    canvas1 = Canvas(frame1, width=700 , height = 500)

    ## 1.BACKGROUND
    
    background1 = Label(canvas1, image=filename1, bd=10)
    background1.pack() 
    canvas1.create_window(350, 250, window=background1)

    square_bg1 = Label(canvas1, width=58 , height=26)
    square_bg1.configure(background = 'burlywood1')
    square_bg1.pack()
    canvas1.create_window(450,250,window=square_bg1)

    ## 2.SHOW DATES
    time_now = str(currenttime.strftime("%a, %d %b, %Y\n%I:%M %p"))
    date1 = Label (canvas1 , text = "\n" + time_now )
    date1.configure(background = 'burlywood1')
    date1.configure( font=("Century Gothic", 16))
    date1.pack()
    canvas1.create_window(450, 280, window=date1)

    ## 3.BUTTON TO TYPE
    def button1func ():
        global_var.dateis = currenttime.strftime("%d/%m/%Y")
        global_var.timeis = currenttime.strftime("%H:%M")
        jump1()
    button1_Input1 = Button(canvas1, text= "  Current Date/Time  ", width=17, height=1, font=("Century Gothic", 14, 'italic'))
    button1_Input1.configure(background = 'old lace')
    button1_Input1.configure(command=button1func)
    button1_Input1.pack()
    canvas1.create_window(350, 350, window=button1_Input1)

    ## 4.BUTTON TO USERDATE
    button1_Input2 = Button(canvas1, text="  Customize Date/Time  ", width=17, font=("Century Gothic", 14,'italic'))
    button1_Input2.configure(background = 'old lace')
    button1_Input2.configure(command=jump2)
    button1_Input2.pack()
    canvas1.create_window(550, 350, window=button1_Input2)

    ## 5.BUTTON TO DESCRIPTIONS
    button1_Input3 = Button(canvas1, text="Descriptions", width=35, font=("Century Gothic", 14, 'italic'))
    button1_Input3.configure(background = 'old lace')
    button1_Input3.configure(command=jump3)
    button1_Input3.pack()
    canvas1.create_window(450, 405, window=button1_Input3)
    
    ## 6.LOGO
    background1 = Label(canvas1, image=filename2, bd=10, width = 150, height = 150)
    background1.pack()
    canvas1.create_window(350, 150, window=background1)

    ##EAT@NS DESCRIPTION
    desc_text = 'Welcome to EAT@NorthSpine! \nHungry for food? \nWith EAT@NorthSpine you can even calculate how long to wait to get your food! Not only that, but you can also sum up how much you need to pay for your food before you get there! '
    desc = Label(canvas1, text = desc_text, bg = 'burlywood1', wrap = 190, font =('Helvetica', 10, 'italic'))
    desc.configure(justify=LEFT, anchor=NW)
    canvas1.create_window(540, 150, window=desc)

    ##-------END--------##
    canvas1.pack()
    return frame1
'''
## TRY TO RUN THE FRAME ##

root = Tk()
root.resizable(False, False)
root.geometry("700x500")
root.title("Canteen of North Spine")

def func1():
    print('yo')
def func2():
    print('yo too')
def func3():
    print('yo tooa')

bg1 = PhotoImage(file = "./folder_images/home.png")
logo = PhotoImage(file = "./folder_images/logo.png")
home_frame = home(root, bg1,logo, func1, func2, func3)
home_frame.pack()'''
