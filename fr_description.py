from tkinter import *
import datetime
from tkinter.messagebox import *
import pickle


file_name="./folder_data/RestMain"
fileObject = open(file_name,'rb')
RestMain = pickle.load(fileObject)


currenttime = datetime.datetime.now()
dateis = currenttime.strftime("%d/%m/%Y")
timeis = currenttime.strftime("%H:%M")


def background(canvas2, y_start, n,titlepic, restpic):
    background2 = Label(canvas2, image=titlepic, border=0)
    background2.pack(side=LEFT, expand=True)
    canvas2.create_window(350, y_start + 20, window=background2)
    for i in range(n):
        background2 = Label(canvas2,image=restpic, border=0)
        background2.pack(side=LEFT, expand=True)
        canvas2.create_window(350, y_start + 100 + i * 120, window=background2)

def scroll(root,rest_list , filename1,filename2 , logos):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=680, height=380)


    y_start = 0
    for i in range(len(rest_list)):
        background(canvas2, y_start, len(rest_list[i][1]), filename1, filename2)
        #storesDesc(canvas2,rest_list)
        y_start += 30 + 120 * len(rest_list[i][1])

    background1 = Label(canvas2, background="gray90", bd=10, width=80, height=y_start, justify=CENTER)
    background1.pack()
    canvas2.create_window(345, 210, window=background1)

    for i in range(len(logos)):
        image1 = Label(canvas2, image=logos[i], bd=10,bg = 'grey90')
        image1.pack()
        canvas2.create_window(155, 150 * i +80, window=image1)

    for i in range(len(rest_list)):
        desc1 = Label(canvas2, text=RestMain[rest_list[i]]['description'], bd=10, anchor=NE)
        desc1.config(wraplength=300,justify=CENTER, bg = "gray90")
        desc1.pack()
        canvas2.create_window(435,150 * i +90, window=desc1)

    for i in range(len(rest_list)):
        title1 = Label(canvas2, text=rest_list[i], width=0, height=0, font=("Helvetica", 16, 'bold'), bg="gray90")
        title1.config(justify=CENTER)
        title1.pack()
        canvas2.create_window(430, 150 * i +40, window=title1)
        
    ## SCROLL
    scroll_y = Scrollbar(frame2, orient="vertical", command=canvas2.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    canvas2.configure(yscrollcommand=scroll_y.set)
    canvas2.configure(scrollregion=(0, 0, 0, y_start))

    canvas2.pack()
    return frame2


def static_header(root):
    frame2 = Frame(root)
    canvas2 = Canvas(frame2, width=700, height=100)

    square_bg1 = Label(canvas2, width=500, height=15)
    square_bg1.configure(background='black')
    square_bg1.pack()
    canvas2.create_window(0, 0, window=square_bg1)


    title1 = Label(text="Stores Overview",
                   fg='white',
                   background="black",
                   font=("fixedsys", 20))
    title1.pack()
    canvas2.create_window(350, 60, window=title1)

    ##-------END--------##
    canvas2.pack()
    return frame2

'''
#### RUN THE FRAME:-------------------------------------------------------
root = Tk()
root.resizable(False, False)
root.geometry("700x500")
root.title("Canteen of North Spine")


bgTitle = PhotoImage(file="./folder_images/titlerest.png")
bgMenu = PhotoImage(file="./folder_images/rests.png")

logos = [PhotoImage(file = "./folder_images/logos/"+i+".png")for i in RestMain]

k = [key_r for key_r in RestMain.keys()]

static_fr = static_header(root)
static_fr.pack()
scroll_fr = scroll(root, k, bgTitle, bgMenu , logos)
scroll_fr.place(x=0,y=115)

root.mainloop()'''

