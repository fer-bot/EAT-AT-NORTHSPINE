#####   TYPERES FRAME   ####
'''
INPUTS:
- root
- filename for background
- filename for restaurant button
- filename for foodcourt button
- function to jump to restaurant_list
- function to jump to foodcourtlist
'''
## IMPORTS ##
from tkinter import *
import datetime
from tkinter.messagebox import *
from functions import*
import pickle

## GLOBAL VARIABLES ##
currenttime = datetime.datetime.now()
dateis = currenttime.strftime("%d/%m/%Y")
timeis = currenttime.strftime("%H:%M")
menu_name=''

## FUNCTIONS ##

def typeRes(root, filename1, res, fc, torest, tofc):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=700 , height = 500)

    ## 1.BACKGROUND
    background1 = Label(canvas2, image=filename1, bd=10)
    background1.pack()
    canvas2.create_window(350, 250, window=background1)
    '''
    square_bg1 = Label(canvas2, width=58 , height=18)
    square_bg1.configure(background = 'grey27')
    square_bg1.pack()
    canvas2.create_window(350,250,window=square_bg1)'''

    ## 2.BUTTONS TO RESTAURANTS
    button1_Input2 = Button(canvas2, text="  RESTAURANTS  ", image=res,compound = CENTER, width=150,height=150, font=("Century Gothic", 14,'bold'))
    button1_Input2.configure(background = 'old lace', foreground = 'white')
    button1_Input2.configure(command=torest)
    button1_Input2.pack()
    canvas2.create_window(255, 250, window=button1_Input2)
    
    ## 3.BUTTONS TO CANTEEN A
    button2_Input2 = Button(canvas2, text="  FOODCOURT  ",image=fc,compound = CENTER, width=150,height=150, font=("Century Gothic", 14,'bold'))
    button2_Input2.configure(background = 'old lace', foreground = 'white')
    button2_Input2.configure(command=tofc)
    button2_Input2.pack()
    canvas2.create_window(445, 250, window=button2_Input2)

    ## 4. Title
    Title3 = Label(frame2, text="Choose The Type:",image = filename1, width=300, height=50, compound=CENTER,font=("Trebuchet MS", 25))
    Title3.configure(foreground = 'gold')
    Title3.place(x=200 , y=100)

    ##------END------##
    canvas2.pack()
    return frame2
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
bg2 = PhotoImage(file = "./folder_images/type.png")
logo = PhotoImage(file = "./folder_images/logo.png")
rest = PhotoImage(file = "./folder_images/restaurant.png")
fc = PhotoImage(file = "./folder_images/foodcourt.png")
typeRes_frame = typeRes(root, bg2, rest, fc, func3, func1)
typeRes_frame.pack()

'''
