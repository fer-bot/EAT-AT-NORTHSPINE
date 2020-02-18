from tkinter import *
import pickle
import global_var
from functions import time_format
from tkinter.messagebox import *
from tkinter.simpledialog import*

file_name="./folder_data/RestMain"
fileObject = open(file_name,'rb')
RestMain = pickle.load(fileObject)


## SHOW OPERATING HOURS
def popout(msg):
    showinfo("Operating Hours" , msg+"\n")
    
def operatingHours(restaurant):
    text = restaurant + "\n"
    store_name = restaurant
    dayOC = RestMain[store_name]["date"]
    for key_dayOC, value_dayOC in dayOC.items():
        if (dayOC[key_dayOC][0] == 0000 and dayOC[key_dayOC][1] == 0000):
            msg = key_dayOC + " : " + "CLOSED"
        else:
            msg = key_dayOC + " : " + str(dayOC[key_dayOC][0]) + " - " + str(dayOC[key_dayOC][1])
        text = text + "\n" + msg
    popout(text)


## SHOW WAITING TIME
def waitCalc(store_name):
    wrong = 0
    while True:
        wait_nonpeak = RestMain[store_name]['wait_nonpeak']
        wait_peak = RestMain[store_name]["wait_peak"] 
        peakHourLunch = [time_format('12:30') , time_format('14:00')]
        peakHourDinner = [time_format('18:30') , time_format('19:30')]

        waitInput = askinteger("Calculate Waiting Time" , "Please enter the number of people in the queue")
        timenow = time_format(global_var.timeis)
        if waitInput:
            if waitInput < 0:
                showwarning('Illegal Value', 'Not valid.\nPlease try again!')
                continue
            elif waitInput >= 30:
                if wrong < 3:
                    showinfo("Error", "Please enter valid number below 30, Attempt: "+ str(wrong+1))
                    wrong +=1
                    continue
                else:
                    showinfo("Error", "Too many attempt! Try Again!")
                    break
            if peakHourLunch[0]<= timenow <=peakHourLunch[1] or peakHourDinner[0]<=timenow<=peakHourDinner[1]:
                result = str(float(wait_peak* waitInput))
                showinfo("Waiting Time", "Waiting Time : " + result + " min")
                global_var.waiting_time = str(result)
                break
            else:
                result = str(float(wait_nonpeak * waitInput))
                showinfo("Waiting Time", "Waiting Time : " + result + " minutes")
                global_var.waiting_time = str(result)
                break
        else:
            break
    
