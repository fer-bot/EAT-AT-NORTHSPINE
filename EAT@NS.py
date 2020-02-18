## IMPORT LIBRARY ##
from tkinter import *
import datetime
from tkinter.messagebox import *
import pickle

## IMPORT FROM OTHER FILES ##
import global_var
from functions import*

from fr_home import home
from fr_top_bar import bar
from fr_userdate import userdate
from fr_description import static_header, scroll
from fr_typeRes import typeRes
from fr_eatery_type import static_header_eatery, eatery_type 
from fr_menu import menu_header, menu_fr
from fr_total import scroll_total, total_fr
from fr_menu_pop_out import operatingHours, waitCalc
########## START ##########

#---Basics---#
root = Tk()
root.resizable(False, False)
root.geometry("700x500")
root.title("Canteen of North Spine")

#---Variables---#

file_name="./folder_data/RestMain"
fileObject = open(file_name,'rb')
RestMain = pickle.load(fileObject)

all_eatery = RestMain.keys()
key = [key_r for key_r in RestMain.keys()]
key.sort()

#---Photos---#

bg1 = PhotoImage(file = "./folder_images/home.png")
logo = PhotoImage(file = "./folder_images/logo.png")

bgTitle = PhotoImage(file="./folder_images/titlerest.png")
bgMenu = PhotoImage(file="./folder_images/rests.png")

homebut = PhotoImage(file = "./folder_images/home_button.png")


logos = [PhotoImage(file = "./folder_images/logos/"+i+".png")for i in key]
logos_dict = {}
for i in key:
    logos_dict[i] = PhotoImage(file = "./folder_images/logos/"+i+".png")

bg2 = PhotoImage(file = "./folder_images/type.png")
rest_logo = PhotoImage(file = "./folder_images/restaurant.png")
fc_logo = PhotoImage(file = "./folder_images/foodcourt.png")

bgOpenClose = PhotoImage(file = "./folder_images/titlerest.png")
bgEateries = PhotoImage(file = "./folder_images/rests.png")

bgMenuTitle = PhotoImage(file = "./folder_images/bgmenu.png")
bgMenuItems = PhotoImage(file = "./folder_images/bgmenu.png")

bg_total = PhotoImage(file = "./folder_images/home.png")

#---Functions---#

def forget_all():
    home_frame.pack_forget()
    userdate_frame.pack_forget()
    desc_static_header.pack_forget()
    desc_scrollable_list.pack_forget()
    choose_type_frame.pack_forget()
    eatery_header.pack_forget()
    fc_frame.pack_forget()
    menu_frame.pack_forget()
    last_fr.pack_forget()
    
## BUTTONS IN HOME FRAME
def home_to_type():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    choose_type_frame.pack()
def home_to_userinput():
    forget_all()
    userdate_frame.pack()
def home_to_desc():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    desc_static_header.pack()
    desc_scrollable_list.pack()
    
## BUTTONS IN TOP BAR    
def bar_to_home():
    global_var.waiting_time = '-'
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    home_frame.pack()
    
## BUTTON ENTER IN USER INPUT FRAME
def userinput_to_type():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    choose_type_frame.pack()
    
## BUTTONS IN CHOOSE RES OR FOODCOURT FRAME
def type_to_rest():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    eatery_header.pack()
    
    rest_stalls = eatery_list(all_eatery, 'r')
    rest_stalls = checkOpen(rest_stalls, global_var.dateis, global_var.timeis)
    
    global_var.all_stalls = [['Open',rest_stalls[0]],['Closed',rest_stalls[1]]]
    global_var.halal_stalls = [['Open', halal_filter(global_var.all_stalls[0][1])],['Closed', halal_filter(global_var.all_stalls[1][1])]]
    global_var.stalls = global_var.all_stalls
    
    eatery_type_frame = eatery_type(fc_frame, bgOpenClose,bgEateries, global_var.stalls,logos_dict, eatery_to_menu)
    eatery_type_frame.place(x=0, y=0)
    fc_frame.pack()
    
def type_to_fc():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    eatery_header.pack()
    
    rest_stalls = eatery_list(all_eatery, 'fc')
    rest_stalls = checkOpen(rest_stalls, global_var.dateis, global_var.timeis)
    
    global_var.all_stalls = [['Open',rest_stalls[0]],['Closed',rest_stalls[1]]]
    global_var.halal_stalls = [['Open', halal_filter(global_var.all_stalls[0][1])],['Closed', halal_filter(global_var.all_stalls[1][1])]]
    global_var.stalls = global_var.all_stalls
    
    eatery_type_frame = eatery_type(fc_frame, bgOpenClose,bgEateries, global_var.stalls,logos_dict, eatery_to_menu)
    eatery_type_frame.place(x=0, y=0)
    fc_frame.pack()
    
## BUTTONS IN STALLS NAMES
def eatery_to_menu():
    global_var.total_price=0
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    
    static_fr = menu_header(menu_frame,global_var.menu_name, menu_veg, menu_all, logos_dict, menu_back, opentime, qtime)
    static_fr.place(y=0)
    
    menu_items = menu(global_var.menu_name, global_var.dateis, global_var.timeis )
    menu_items = sort_by_price(menu_items, global_var.menu_name)
    thelist = cat_and_items(global_var.menu_name, menu_items)
    menu_frm = menu_fr(menu_frame, bgMenuTitle,bgMenuItems,thelist,global_var.menu_name,proceed)
    menu_frm.place(x = 0, y = 130)
    menu_frame.pack()

def eatery_hallal():
    forget_all()
    
    eatery_header.pack()
    global_var.stalls = global_var.halal_stalls
    
    eatery_type_frame = eatery_type(fc_frame, bgOpenClose,bgEateries, global_var.stalls,logos_dict, eatery_to_menu)
    eatery_type_frame.place(x=0, y=0)
    fc_frame.pack()
    
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)

def eatery_all_type():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    eatery_header.pack()
    
    global_var.stalls = global_var.all_stalls

    eatery_type_frame = eatery_type(fc_frame, bgOpenClose,bgEateries, global_var.stalls,logos_dict, eatery_to_menu)
    eatery_type_frame.place(x=0, y=0)
    fc_frame.pack()
def eatery_back():
    userinput_to_type()

def search():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    eatery_header.pack()
    
    search_list = global_var.all_stalls[0][1]+global_var.all_stalls[1][1]
    search_list.sort()
    item = [['Item Found:', binarySearch(search_list, global_var.search)]]

    eatery_type_frame = eatery_type(fc_frame, bgOpenClose,bgEateries, item ,logos_dict, eatery_to_menu)
    eatery_type_frame.place(x=0, y=0)
    fc_frame.pack()
    
## BUTTONS IN MENU FRAME
def menu_all():
    eatery_to_menu()
    
def menu_veg():
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    
    static_fr = menu_header(menu_frame,global_var.menu_name, menu_veg, menu_all, logos_dict, menu_back, opentime, qtime)
    static_fr.place(y=0)
    
    menu_items = menu(global_var.menu_name, global_var.dateis, global_var.timeis )
    menu_items = veg_filter(menu_items, global_var.menu_name)
    menu_items = sort_by_price(menu_items, global_var.menu_name)
    thelist = cat_and_items(global_var.menu_name, menu_items)
    menu_frm = menu_fr(menu_frame, bgMenuTitle,bgMenuItems,thelist,global_var.menu_name,proceed)
    menu_frm.place(x = 0, y = 130)
    menu_frame.pack()
    
def proceed():
    total_lists()
    forget_all()
    total_frame = total_fr(last_fr, bg_total, destroy, total_back)
    total_frame.pack()

    total = Label(last_fr, text="Total Cost: S$ " + str(global_var.total_price) , font=("fixedsys", 18))
    total.configure(fg='white', bg='salmon3', anchor = W, justify=LEFT, width = 25)
    total.place(x=250, y=350)
    
    wait = Label(last_fr, text="Queue Time: " + str(global_var.waiting_time)+" minutes" , font=("Arial", 12))
    wait.configure(fg='white', bg='black', width = 25)
    wait.place(x=2, y=40)
    
    scroll_fr = scroll_total(last_fr)
    scroll_fr.place(x=245,y=85)
    last_fr.pack()
    
def menu_back():
    forget_all()
    global_var.waiting_time = '-'
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    eatery_header.pack()
    eatery_type_frame = eatery_type(fc_frame, bgOpenClose,bgEateries, global_var.stalls,logos_dict, eatery_to_menu)
    eatery_type_frame.place(x=0, y=0)
    fc_frame.pack()
    
def opentime():
    operatingHours(global_var.menu_name)

def qtime():
    waitCalc(global_var.menu_name)

## BUTTONS IN TOTAL FRAME
def destroy():
    root.destroy()

def total_back():
    global_var.total_price=0
    forget_all()
    top_bar_frame = bar(root, homebut, bar_to_home)
    top_bar_frame.place(y = 0)
    
    static_fr = menu_header(menu_frame,global_var.menu_name, menu_veg, menu_all, logos_dict, menu_back, opentime, qtime)
    static_fr.place(y=0)
    
    menu_items = menu(global_var.menu_name, global_var.dateis, global_var.timeis )
    menu_items = sort_by_price(menu_items, global_var.menu_name)
    thelist = cat_and_items(global_var.menu_name, menu_items)
    menu_frm = menu_fr(menu_frame, bgMenuTitle,bgMenuItems,thelist,global_var.menu_name,proceed)
    menu_frm.place(x = 0, y = 130)
    menu_frame.pack()

#---Frames---#
home_frame = home(root, bg1,logo, home_to_type, home_to_userinput, home_to_desc)
userdate_frame = userdate(root, bg1, userinput_to_type)
desc_static_header = static_header(root)
desc_scrollable_list = scroll(root, key, bgTitle, bgMenu , logos)
choose_type_frame = typeRes(root, bg2,rest_logo, fc_logo,type_to_rest, type_to_fc)
eatery_header = static_header_eatery(root, eatery_hallal, eatery_all_type,eatery_back, search)
fc_frame = Frame(root, width = 700, height = 400)
menu_frame = Frame(root,width = 700, height = 600)
last_fr = Frame(root, width = 700, height = 600)

top_bar_frame = bar(root, homebut, bar_to_home)
top_bar_frame.place(y = 0)


home_frame.pack()
root.mainloop()
