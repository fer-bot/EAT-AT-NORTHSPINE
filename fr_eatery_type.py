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
## GLOBAL VARIABLES ##
file_name="./folder_data/RestMain"
fileObject = open(file_name,'rb')
RestMain = pickle.load(fileObject)


## FUNCTIONS 1 ##

def static_header_eatery(root, eatery_hallal, eatery_all, eatery_back, search):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=700, height=115)

    square_bg1 = Label(canvas2, width=500, height=15)
    square_bg1.configure(background='black')
    square_bg1.pack()
    canvas2.create_window(0, 0, window=square_bg1)

    ###TITLE###
    title1 = Label(text="List of Stores",
                   fg='white',
                   background="black",
                   font=("fixedsys", 30, 'bold'))
    title1.pack()
    canvas2.create_window(350, 40, window=title1)
    

    ###BUTTON HALAL###
    def Halal():
        eatery_hallal()
    
    Halal_button = Button(canvas2,
                          text = 'Halal',
                          command = Halal,
                          height = 1,
                          width = 4)
    canvas2.create_window(200, 90, window=Halal_button)
    
    ###BUTTON ALL###
    def All():
        eatery_all()
    
    All_button = Button(canvas2,
                        text = 'All',
                        command = All,
                        height = 1,
                        width = 4)
    canvas2.create_window(250, 90, window=All_button)

    ###BUTTON BACK###
    def Back():
        eatery_back()
    
    All_button = Button(canvas2,
                        text = 'Back',
                        command = Back,
                        height = 1,
                        width = 4,
                        bg = 'red',
                        font = ('Helvetica', 10,'bold'))
    canvas2.create_window(660, 40, window=All_button)

    ###SEARCH BAR###
    
    search_bar = Entry(canvas2)
    canvas2.create_window(420, 90, window=search_bar)
    def search_fn():
        global_var.search = search_bar.get()
        search()
    Search_button = Button(canvas2, text = 'Search', command = search_fn, height = 1, width = 5)
    canvas2.create_window(550, 90, window=Search_button)

    ##-------END--------##
    canvas2.pack()
    return frame2

## FUNCTIONS 2 ##

def background(canvas2,y_start, n, titlepic, restpic):
    background2 = Label(canvas2, image=titlepic, border=0)
    background2.pack(side=LEFT, expand=True)
    canvas2.create_window(350, y_start+20, window=background2)
    for i in range (n):
        background2 = Label(canvas2, image=restpic, border=0)
        background2.pack(side=LEFT, expand=True)
        canvas2.create_window(350, y_start+100+i*120, window=background2)
        
def makebutton(canvas2, title, res_list_menu, y_start, logos_dict, function, frame2):
    #make a black bg for desc
    desc_label = Label(frame2,  font=('Arial',10), width = 20, height=30)
    desc_label.configure(bg = 'grey10')
    desc_label.place(x=450, y=8)
    
    #--------To jump to other frame
    def jump(i, function):
        global_var.menu_name = res_list_menu[i]
        canvas2.yview_scroll(2, 'units')
        function()
        
    #-------make desc appear when the mouse enter the button
    def box_description(i):
        desc_label = Label(frame2, anchor=NW, pady=0)
        desc_label.configure(text= '-'*20+'\n' +res_list_menu[i].upper() + '\n\n' +\
                             'Description: \n'+ rest_dict[res_list_menu[i]]['description']+ '\n\n'\
                             'Category: \n' + print_category(rest_dict[res_list_menu[i]]['category']) +\
                             '\n' + '-'*20)
        desc_label.configure(font=('Times New Roman',12), width = 20, height=30, justify = LEFT)
        desc_label.configure(bg='grey10',fg='old lace',wraplength=170)
        desc_label.place(x=450, y=8)
        
    #------Make the open and close title
    title_bar = Label (canvas2 , text = title )
    title_bar.configure( font=("Helvetica", 19, 'bold'), background = 'grey10', foreground = 'white')
    title_bar.pack()
    canvas2.create_window(250, y_start+20, window=title_bar)
    
    #------Remove the description if cursor not in the button
    def make_black():
        desc_label = Label(frame2, font=('Arial',10), width = 21, height=30)
        desc_label.configure(bg = 'grey10')
        desc_label.place(x=450, y=8) 
    #------Make the food button
    for i in range (len(res_list_menu)):
        #make the box of Description
        images = logos_dict[res_list_menu[i]]
        #make the button
        button1_Input2 = Button(canvas2,padx=30,anchor=W, text=res_list_menu[i],wrap = 200,justify=LEFT)
        button1_Input2.configure(image=images, compound = LEFT, width=300, height=100, font=("courier new", 16, 'bold'), command=None)
        button1_Input2.configure(command = lambda i=i:jump(i, function))
        button1_Input2.pack(side=LEFT)
        button1_Input2.bind('<Enter>', lambda event, i=i:box_description(i))
        button1_Input2.bind('<Leave>', lambda event:make_black())
        canvas2.create_window(250, y_start+100+120*i, window=button1_Input2)

def eatery_type(root,filename1, filename2, list_of_type_and_foods, logos_dict, button_func):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=680 , height = 370, background = 'grey10')

    ## 1.BACKGROUND
    y_start=0
    for i in range (len(list_of_type_and_foods)):
        background(canvas2,y_start, len(list_of_type_and_foods[i][1]), filename1, filename2)
        makebutton(canvas2,'-'*10+list_of_type_and_foods[i][0]+'-'*10, list_of_type_and_foods[i][1],y_start, logos_dict, button_func, frame2)
        y_start += 20+120*len(list_of_type_and_foods[i][1])+20
    
    ##----scrollable----##
    scroll_y2 = Scrollbar(frame2, orient="vertical", command=canvas2.yview)
    scroll_y2.pack(side=RIGHT, fill=Y)
    canvas2.configure(yscrollcommand=scroll_y2.set)
    canvas2.configure(scrollregion=(0,0,0,y_start+10))

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
    print('yo')
def func2():
    print('yo too')
def func3():
    static_fr.pack()
    eatery_type_frame.pack()
    home_frame.pack_forget()
def button_function():
    eatery_type_frame.pack_forget()
    home_frame.pack()
    static_fr.pack_forget()

bg1 = PhotoImage(file = "./folder_images/home.png")
bgTitle = PhotoImage(file = "./folder_images/titlerest.png")
bgMenu = PhotoImage(file = "./folder_images/rests.png")
rest = PhotoImage(file = "./folder_images/restaurant.png")
fc = PhotoImage(file = "./folder_images/foodcourt.png")
logo = PhotoImage(file = "./folder_images/logo.png")

k = [key_r for key_r in RestMain.keys()]
k.sort()
logos = [PhotoImage(file = "./folder_images/logos/"+i+".png")for i in k]
logos_dict = {}
for i in k:
    logos_dict[i] = PhotoImage(file = "./folder_images/logos/"+i+".png")


thelist= [['Open',['Miniwok','Vegetarian','Subway','Umisushi']],['Closed',['Western','KFC','McDonald\'s','Mixrice']]]

home_frame = home(root, bg1,logo, func1, func2, func3)

image_list=[]
for i in range (len(thelist)):
    image_list.append([])
    for j in (thelist[i][1]):
        image_list[i].append(PhotoImage(file = "./folder_images/logos/"+ j +".png"))
#print(image_list)

static_fr = static_header_eatery(root, func1, func2, func1)
static_fr.pack()
eatery_type_frame = eatery_type(root, bgTitle,bgMenu,thelist,logos_dict, button_function)
eatery_type_frame.pack()
'''
