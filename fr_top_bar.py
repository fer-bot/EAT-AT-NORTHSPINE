#####   BAR FRAME   ####
'''
INPUTS:
- root
- file name of home_button
- function to direct home button to home
'''
## IMPORTS ##
from tkinter import *
import datetime
from tkinter.messagebox import *
from functions import*
import pickle
import global_var

from fr_userdate import userdate
## FUNCTIONS ##

def bar(root, home_button, function):
    frame2 = Frame(root)
    square_bg1 = Label(frame2, text = "Date: " +global_var.dateis + ', Time: ' + global_var.timeis + " "*110 , font = ("Century Gothic", 12,'bold'),justify= LEFT,  width=100 , height=1)
    square_bg1.configure(background = 'gray27', foreground='white')
    square_bg1.pack()
    button2_Input2 = Button(frame2 ,image=home_button, width=15,height=15)
    button2_Input2.configure(background = 'white', foreground = 'white')
    button2_Input2.configure(command=function)
    button2_Input2.place(x=670, y=2)
    ##------END------##
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

homebut = PhotoImage(file = "./folder_images/home_button.png")
bar_frame =bar(root, homebut, func1)
bar_frame.pack()


bg1 = PhotoImage(file = "./folder_images/home.png")
logo = PhotoImage(file = "./folder_images/logo.png")
userdate_frame = userdate(root, bg1, func3)
userdate_frame.pack()'''
