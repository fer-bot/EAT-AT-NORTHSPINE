#####   FOODCOURT OR RESTAURANT FRAME   ####
'''
INPUTS:
- root
- file name of open and close title
- file name of restaurant button
- list with [['Open',['miniwok','vegetarian','subway','umisushi']],['Closed',['western','kfc','mcdonalds','mixrice']]] format
- image list
- function to jump to other frame
'''
## IMPORTS ##
from tkinter import *
import datetime
from tkinter.messagebox import *
from functions import*
import pickle
from fr_home import home
import global_var

file_name="./folder_data/RestMain"
fileObject = open(file_name,'rb')
RestMain = pickle.load(fileObject)

## GLOBAL VARIABLES ##

## FUNCTIONS 1 ##

def menu_header(root, stall_name, Veg, All, logo_dict, back, opentime, qtime):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=700, height=130)

    ###BG###
    square_bg1 = Label(canvas2, width=500, height=20)
    square_bg1.configure(background='navajo white')
    square_bg1.pack()
    canvas2.create_window(0, 0, window=square_bg1)

    ###LOGO###
    logo_place = Label(canvas2, image = logo_dict[stall_name], bd = 5)
    logo_place.pack()
    canvas2.create_window(61, 80, window=logo_place)
 

    ###TITLE###
    title1 = Label(text=stall_name,
                   fg='white',
                   background="navajo white",
                   font=("fixedsys", 40, 'bold'))
    title1.pack()
    canvas2.create_window(350, 65, window=title1)
    

    ###BUTTON VEG###
    Veg_button = Button(canvas2,
                        text = 'Veg',
                        command = Veg,
                        height = 1,
                        width = 4)
    canvas2.create_window(325, 110, window=Veg_button)
    
    ###BUTTON ALL###
    All_button = Button(canvas2,
                        text = 'All',
                        command = All,
                        height = 1,
                        width = 4)
    canvas2.create_window(375, 110, window=All_button)

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
    canvas2.create_window(660, 40, window=All_button)

    ###BUTTON OPERATING HOURS###
    def openT():
        opentime()
    
    All_button = Button(canvas2,
                        text = 'Operating Hours',
                        command = openT,
                        height = 1, width = 15,
                        font = ('Helvetica', 10,'italic'))
    canvas2.create_window(620, 85, window=All_button)

    ###BUTTON QUEUEING TIME###
    def que():
        qtime()
    
    All_button = Button(canvas2,
                        text = 'Check Queue Time',
                        command = que,
                        height = 1, width=15,
                        font = ('Helvetica', 10,'italic'))
    canvas2.create_window(620,115, window=All_button)
    
    ##-------END--------##
    canvas2.pack()
    return frame2


## FUNCTIONS 2 ##

def total(total,frame2):
    tot_label = Label(frame2, text="TOTAL : S$ " + str(total), width = 50, anchor=W,borderwidth=2,relief='groove')
    tot_label.configure(font=('Courier New',15,'bold'),bg='white',padx=10,pady=5)
    tot_label.place(x=20,y=330)
    
def proc(frame2, proceed):
    enter_button = Button(frame2, text="PROCEED" , bg = 'green' , fg='white',font = ('Courier New', 15, 'bold'))
    enter_button.configure(command = proceed)
    enter_button.place(x=570, y=280)
    
def background(canvas2,y_start, n, menubg):
    background2 = Label(canvas2, image=menubg, border=0)
    background2.pack(side=LEFT, expand=True)
    canvas2.create_window(350, y_start+25, window=background2)
    for i in range (n):
        background2 = Label(canvas2, image=menubg, border=0)
        background2.pack(side=LEFT, expand=True)
        if i%2 == 0:
            canvas2.create_window(350+50, y_start+75+i*50, window=background2)
        else:
            canvas2.create_window(350-70, y_start+75+i*50, window=background2)

def menu_sfr(frame2, canvas2, res_name,title, menu_list,y_start,buy_list, proceed):
    #import dictionary
    file_name="./folder_data/menus/"+res_name
    fileObject = open(file_name,'rb')
    menu_dict = pickle.load(fileObject)
    #make the title
    type_label = Label(canvas2,text = title, width = 200)
    type_label.configure(font=("Century Gothic", 19, 'bold'), background = 'old lace', foreground = 'grey10')
    type_label.pack()
    canvas2.create_window(350, y_start+22, window=type_label)
    for i in menu_list:
        buy_list.append([i,0])
    #make the menu labels per title
    counter=[IntVar() for i in range(len(menu_list))]
    for i in range(len(menu_list)):
        x=0
        menu_label = Label(canvas2,padx=0,anchor=W, text= menu_list[i],justify=LEFT, width = 60,)
        menu_label.configure(font=("Century Gothic", 12, 'italic','bold'),wraplength=200, bg='old lace')
        menu_label.pack()
        canvas2.create_window(350, y_start+72+50*i, window=menu_label)
        price_label = Label(canvas2,padx=0,anchor=W, text='S$ '+ str(menu_dict[menu_list[i]]['price']),justify=LEFT)
        price_label.configure(font=("courier new", 16, 'italic'),wraplength=200, bg='old lace')
        price_label.pack()
        canvas2.create_window(350, y_start+72+50*i, window=price_label)
        #Quantity Button
        def inc(i):
            if buy_list[i][1] >= 0:
                counter[i].set(counter[i].get() + 1)
                buy_list[i][1] = counter[i].get()
                global_var.total_price+= menu_dict[menu_list[i]]['price']
                global_var.total_price = round(global_var.total_price,1)
                #print(total_price,buy_list)
                total(global_var.total_price,frame2)
            else:
                buy_list[i][1] = 0

        def dec(i):
            if (buy_list[i][1] > 0):
                counter[i].set(counter[i].get() - 1)
                buy_list[i][1] = counter[i].get()
                global_var.total_price -= menu_dict[menu_list[i]]['price']
                global_var.total_price = round(global_var.total_price,1)
                #print(buy_list_i)
                total(global_var.total_price,frame2)
            
        LabelItem = Label(canvas2,textvariable=counter[i])
        canvas2.create_window(525, y_start+72+50*i, window=LabelItem)
        B1=Button(canvas2,text="-", command=lambda i=i:dec(i))
        B1.pack()
        B2=Button(canvas2,text="+", command=lambda i=i:inc(i))
        B2.pack()
        canvas2.create_window(500, y_start+72+50*i, window=B1)
        canvas2.create_window(550, y_start+72+50*i, window=B2)    
    #make the total
    total(global_var.total_price,frame2)
    proc(frame2,proceed)

def menu_fr(root,filename1, filename2, list_of_type_and_foods,res_name,proceed):
    global_var.total_price = 0
    global_var.buy_list =[]
    
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=680 , height = 400, background = 'white')

    ## 1.BACKGROUND AND MENU
    y_start=0
    global_var.buy_list = []
    for i in range (len(list_of_type_and_foods)):
        global_var.buy_list.append([])
        background(canvas2,y_start, len(list_of_type_and_foods[i][1]), filename1)
        menu_sfr(frame2,canvas2,res_name,'-'*10+' '+list_of_type_and_foods[i][0]+" "+'-'*10, list_of_type_and_foods[i][1],y_start,global_var.buy_list[i],proceed)
        y_start += 50+50*len(list_of_type_and_foods[i][1])
    background(canvas2,y_start,1,filename1)
    y_start +=50
        
    ##----scrollable----##
    scroll_y2 = Scrollbar(frame2, orient="vertical", command=canvas2.yview)
    scroll_y2.pack(side=RIGHT, fill=Y)
    canvas2.configure(yscrollcommand=scroll_y2.set)
    canvas2.configure(scrollregion=(0,0,0,y_start+20))

    ##-------END--------##
    canvas2.pack()
    return frame2
'''
## TRY TO RUN THE FRAME ##
root = Tk()
root.resizable(False, False)
root.geometry("700x500")
root.title("Canteen of North Spine")

def func1():
    print(global_var.buy_list)
def func2():
    print(global_var.total_price)
def func3():
    print(menu_name)
    foodcourt_frame.pack()
    home_frame.pack_forget()
def button_function():
    home_frame.pack()

bg1 = PhotoImage(file = "./folder_images/home.png")
bgTitle = PhotoImage(file = "./folder_images/bgmenu.png")
bgMenu = PhotoImage(file = "./folder_images/bgmenu.png")

thelist= [['Food',['Burger','Burger','Frenchfries','Iced Latte']],\
          ['Drink',['Hot Milo','Iced Latte','Hot Milo','Iced Latte','Hot Milo','Iced Latte']],\
          ['what',['Hot Milo','Iced Latte','Hot Milo','Iced Latte','Hot Milo','Iced Latte']]]

store_name = 'KFC'
file_name = "./folder_images/logos/" +store_name+ ".png"
logo = PhotoImage(file = file_name)

key = [key_r for key_r in RestMain.keys()]
key.sort()
logos = [PhotoImage(file = "./folder_images/logos/"+i+".png")for i in key]
logos_dict = {}
for i in key:
    logos_dict[i] = PhotoImage(file = "./folder_images/logos/"+i+".png")


filename2 = PhotoImage(file = "./folder_images/home.png")

menu_file_name="./folder_data/menus/" + store_name
fileObject = open(menu_file_name,'rb')
rest_menu = pickle.load(fileObject)

menu_list = menu('KFC', global_var.dateis, '15:10')
print(menu_list)
static_fr = menu_header(root,'McDonald\'s', func1, func2, logos_dict)

static_fr.pack()

res_name = 'McDonald\'s'
menu_fr = menu_fr(root, bgTitle,bgMenu,thelist,res_name)
menu_fr.pack()'''
