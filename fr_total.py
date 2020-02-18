from tkinter import *
import datetime
from tkinter import messagebox
import global_var




def scroll_total(root):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=390, height=245 , background = "burlywood1")
    length = 13
    
    ##CONTENT
    for i in range(len(global_var.final_items)):
        box = Label(canvas2, bg='burlywood2', width = 43, text = ' '*3 + global_var.final_items[i], fg = 'black',height = 1, anchor=NW)
        box.configure(font = ('Calibri',13,'bold'), wrap=230, justify = LEFT)
        box.pack()
        canvas2.create_window(195,length, window=box)
        
        box = Label(canvas2, bg='burlywood2', text = global_var.final_ammount[i], fg = 'black',height = 1, anchor=N)
        box.configure(font = ('Calibri',11,'italic'), justify = LEFT)
        box.pack()
        canvas2.create_window(270,length, window=box)

        box = Label(canvas2, bg='burlywood2', text = global_var.final_prices[i], fg = 'black',height = 1, anchor=NW)
        box.configure(font = ('Calibri',13,'bold'), justify = LEFT)
        box.pack()
        canvas2.create_window(345,length, window=box)
        
        length+=28
        
    ## SCROLL
    scroll_y = Scrollbar(frame2, orient="vertical", command=canvas2.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    canvas2.configure(yscrollcommand=scroll_y.set)
    canvas2.configure(scrollregion=(0, 0, 0, length))
    
    canvas2.pack()
    return frame2

def total_fr(root, filename1,destroy, back):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=700, height=500)

    ## 1.BACKGROUND
    background1 = Label(canvas2, image=filename1, bd=10)
    background1.pack()
    canvas2.create_window(350, 250, window=background1)

    square_bg1 = Label(canvas2, width=60, height=25)
    square_bg1.configure(background='grey30')
    square_bg1.pack()
    canvas2.create_window(450, 220, window=square_bg1)

    square_bg1 = Label(canvas2, width=58, height=16)
    square_bg1.configure(background='burlywood1')
    square_bg1.pack()
    canvas2.create_window(450, 212, window=square_bg1)

    square_bg1 = Label(canvas2, width=58, height=4)
    square_bg1.configure(background='salmon3')
    square_bg1.pack()
    canvas2.create_window(450, 370, window=square_bg1)

    square_bg1 = Label(canvas2, width=58, height=3)
    square_bg1.configure(background='burlywood1')
    square_bg1.pack()
    canvas2.create_window(450, 65, window=square_bg1)

    ## 2.Total price 
    total = Label(canvas2, text="Total Cost: S$ " + str(global_var.total_price) , font=("fixedsys", 18))
    total.configure(fg='white', bg='salmon3', anchor = W, justify=LEFT, width = 25)
    total.pack()
    canvas2.create_window(450, 370, window=total)

    ## 2. Title
    Title3 = Label(frame2, text="Order Summary :", font=("fixedsys", 20), background='burlywood1')
    Title3.place(x=260, y=45)

    ###BUTTON BACK###
    def Back():
        back()
    
    All_button = Button(canvas2,
                        text = 'Back',
                        command = Back,
                        height = 1,
                        width = 4,
                        bg = 'red',
                        font = ('Helvetica', 10,'bold'))
    canvas2.create_window(660, 430, window=All_button)
    
    ## EXIT
    def close_window():
        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',icon='warning')
        if MsgBox == 'yes':
            destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
        
    exit_button = Button(root,text="Exit",
                         command=close_window,
                         fg='white',
                         bg='red4',
                         font=("Helvectica", 17),
                         border=0)

    exit_button.pack(fill=BOTH, side=BOTTOM)

    canvas2.pack()
    return frame2

    ##------END------##

'''
#### RUN THE FRAME:-------------------------------------------------------
root = Tk()
root.resizable(False, False)
root.geometry("700x500")
root.title("Canteen of North Spine")

bg_total = PhotoImage(file = "./folder_images/home.png")
total_frame = total_fr(root, bg_total)
total_frame.pack()
scroll_fr = scroll(root)
scroll_fr.place(x=245,y=85)

root.mainloop()'''
