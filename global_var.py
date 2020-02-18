from tkinter import *
import datetime
from tkinter.messagebox import *
from functions import*
import pickle


## GLOBAL VARIABLES ##
currenttime = datetime.datetime.now()

dateis = currenttime.strftime("%d/%m/%Y")
timeis = currenttime.strftime("%H:%M")

all_stalls = []
halal_stalls = []
stalls = []

menu_name=''

search = ''
total_price = 0.0
buy_list = []

final_items = []
final_ammount = []
final_prices =[]

waiting_time = '-'
