#####   USERDATE FRAME   ####
'''
INPUTS:
- root 
- image file name for the background
- function to forget this frame and pack another frame
'''
## IMPORTS ##
from tkinter import *
import datetime
from tkinter.messagebox import *
from functions import*
import pickle
import global_var

currenttime = datetime.datetime.now()
## FUNCTIONS ##

def userdate(root, filename1, function):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=700 , height = 500)

    ## 1.BACKGROUND
    background1 = Label(canvas2, image=filename1, bd=10)
    background1.pack()
    canvas2.create_window(350, 250, window=background1)

    square_bg1 = Label(canvas2, width=60 , height=19)
    square_bg1.configure(background = 'grey30')
    square_bg1.pack()
    canvas2.create_window(450,250,window=square_bg1)
    
    square_bg1 = Label(canvas2, width=58 , height=18)
    square_bg1.configure(background = 'burlywood1')
    square_bg1.pack()
    canvas2.create_window(450,250,window=square_bg1)

    ## 2. Title
    Title3 = Label(frame2, text="Enter Date and Time :",font=("fixedsys", 20), background = 'burlywood1')
    Title3.place(x=280 , y=140)

    ## 3. Take Input1 
    Title3_Date = Label(frame2, text="Insert Date  :",font=("Helvetica", 14, 'italic'),background = 'burlywood1')
    Title3_Date.place(x=310 , y=200)
    enter3_input1 = Entry(frame2, bd=4 ,font=("Helvetica", 13, 'italic'), width=13)
    enter3_input1.insert(0,global_var.dateis)
    enter3_input1.place(x = 460, y=200) 

    ## 4. Take Input2
    Title3_Time = Label(frame2, text="Insert Time :",font=("Helvetica", 14, 'italic'),background = 'burlywood1')
    Title3_Time.place(x=310 , y=250)
    enter3_input2 = Entry(frame2, bd=4 ,font=("Helvetica", 15, 'italic'), width=11)
    enter3_input2.insert(0,global_var.timeis)
    enter3_input2.place(x = 460, y=250)

    ## 5. Enter Button
    def prompt_error():
        showerror("Date and Time Error", "The date or time you type in is Invalid") 
    def evaluate():
        #global dateis
        #global timeis
        date = enter3_input1.get()
        time = enter3_input2.get()
        if checkdate(date) and checktime(time):
            global_var.dateis = date
            global_var.timeis = time
            function()
        else:
                    prompt_error()
    button3_Input = Button(frame2, text='Enter',font=("fixedsys", 13), height = 2, width=10, command = evaluate)
    button3_Input.place (x=400, y=310)

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
    print(dateis)
def func2():
    print('yo too')
def func3():
    print('yo tooa')

bg1 = PhotoImage(file = "./folder_images/home.png")
logo = PhotoImage(file = "./folder_images/logo.png")
userdate_frame = userdate(root, bg1, func1)
userdate_frame.pack()'''
