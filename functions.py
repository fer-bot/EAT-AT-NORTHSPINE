####-------------IMPORT-----------------#####
import pickle
import datetime
import global_var

file_name="./folder_data/RestMain"
fileObject = open(file_name,'rb')
rest_dict = pickle.load(fileObject)
###------------FUNCTIONS----------------####

#1.CHECK DATE AND TIME
#Check date
def checkdate(dateis):
	if len(dateis) !=10:
		return False
	date_lst = list(dateis.split('/'))

	if len(date_lst) !=3:
		return False

	try:
		for i in range(len(date_lst)):
			date_lst[i] = int(date_lst[i])
	except:
		return False

	try:
		datetime.datetime(date_lst[2],date_lst[1],date_lst[0])
		return True
	except ValueError :
		return False
#Check time
def checktime(timeis):
	if len(timeis) !=5:
		return False
	time_lst = list(timeis.split(":"))
	if len(time_lst)!=2:
		return False
	try:
		for i in range(len(time_lst)):
			time_lst[i] = int(time_lst[i])
	except:
		return False
	if 0<= time_lst[0]<=23 and 0<=time_lst[1]<=59:
		return True
	else:
		return False
#Check both time and date exist
def check_date_and_time(dateis,timeis):
	return (checkdate(dateis) and checktime(timeis))


#2.SORT BASED ON PRICE
#To make [food , price] list to be sorted later on
def make_NamePrice_list(food_list,rest):
    return list([i, rest[i]['price']] for i in food_list)  
#To merge two sorted list to be used in the recrusion function later on
def merge_two_rest_list(left_list , right_list):
    final_list = []
    while not(left_list== []) and not(right_list ==[]):
        if left_list[0][1] < right_list[0][1]:
            final_list.append(left_list[0])
            left_list.pop(0)
        else:
            final_list.append(right_list[0])
            right_list.pop(0)
    final_list = final_list + left_list + right_list
    return final_list           
#To sort in [food, price] format
def recrusive_sorting (food_price_list):
    if len(food_price_list) < 2:
        return food_price_list
    else:
        n = len(food_price_list)//2
        return merge_two_rest_list(recrusive_sorting(food_price_list[:n]),recrusive_sorting(food_price_list[n:]))
#Return sorted list but just the food name without the price
def sort_by_price(food_list, res_name):
    file_name="./folder_data/menus/" + res_name
    fileObject = open(file_name,'rb')
    rest = pickle.load(fileObject)
    food_price_list = make_NamePrice_list(food_list,rest)
    return list(i[0] for i in recrusive_sorting(food_price_list))


#3.RETURN DAY OF THE DATE
def date_to_day(date):
    return str(datetime.datetime.strptime(date, "%d/%m/%Y").strftime('%a'))


#4.FORMAT TIME TO INTEGER 
def time_format(time_str):
    return int(time_str[0:2] + time_str[3:])


#5.CHECK RESTAURANT THAT OPEN
def checkOpen(lst, date, time):
    Open_rest = []
    Closed_rest = []
    day = date_to_day(date)
    for restaurant in lst:
        open_times = rest_dict[restaurant]['date'][day]
        if open_times[0]<=time_format(time)<=open_times[1]:
            Open_rest.append(restaurant)
        else:
            Closed_rest.append(restaurant)
    Open_rest.sort()
    Closed_rest.sort()
    return [Open_rest, Closed_rest]


#6.CHECK HALAL RESTAURANT
def halal_filter(list_rest):
    All_rest = []
    for restaurant in list_rest:
        halal = rest_dict[restaurant]['category']
        if halal == 'H':
            All_rest.append(restaurant)
    return All_rest


#7.CHECK MENU IN A RESTAURANT
def menu(restaurant, date, time):
    items_list = []
    #open the menu file
    file_name="./folder_data/menus/" + restaurant
    fileObject = open(file_name,'rb')
    rest_menu = pickle.load(fileObject)
    #then check the available items
    day = date_to_day(date)
    for item in rest_menu:
        item_dict = rest_menu[item]
        if (day in item_dict['day']) and (item_dict['time'][0]<=time_format(time)<=item_dict['time'][1]):
            items_list.append(item)
    return (items_list)

#8.CHECK VEGETARIAN RESTAURANTS 
def veg_filter(menu_list, res_name):
    #open the menu file
    file_name="./folder_data/menus/" + res_name
    fileObject = open(file_name,'rb')
    rest_menu = pickle.load(fileObject)
    #then check the available items
    veg_list = []
    for item in menu_list:
        if rest_menu[item]['veg'] == 1:
            veg_list.append(item)
    return(veg_list)

#9.PRINT CATEGORY
def print_category(cat):
        if cat == 'H':
                return 'Halal'
        elif cat == 'V':
                return 'Vegetarian'
        else:
                return'Non-Halal'

#10.LIST RESTAURANTS OR FC
def eatery_list(lst, rfc):
    the_list = []
    for i in lst:
        if rest_dict[i]['location'] == rfc:
            the_list.append(i)
    the_list.sort()
    return the_list

#11.LIST OF CATEGORY AND MENU ITEMS:
def cat_and_items(res_name, lst):
    #menu dict
    file_name="./folder_data/menus/" + res_name
    fileObject = open(file_name,'rb')
    rest_menu = pickle.load(fileObject)
    #make the list
    cat = []
    item_list = []
    
    for i in lst:
        type_cat = rest_menu[i]['type']
        if type_cat in cat:
            item_list[cat.index(type_cat)].append(i)
        else:
            cat.append(rest_menu[i]['type'])
            item_list.append([i])
        
    combine = []
    for i in range (len(cat)):
        combine.append([cat[i],item_list[i]])
    return combine

#12.TOTAL OF ALL
def total_lists():
    global_var.final_items = []
    global_var.final_ammount = []
    global_var.final_prices =[]
    
    #open the menu file
    file_name="./folder_data/menus/" + global_var.menu_name
    fileObject = open(file_name,'rb')
    rest_menu = pickle.load(fileObject)
    
    #make the list
    for i in global_var.buy_list:
        for j in i:
            if j[1] != 0 :
                global_var.final_items.append(j[0])
                global_var.final_ammount.append("x " + str(j[1]))
                global_var.final_prices.append("S$ " + str(round(j[1] * rest_menu[j[0]]['price'],1) ))


#13.SEARCH THE MENU
def binarySearch(items, target):
    items_upper = [x.upper() for x in items]
    target_upper = target.upper()
    found=[]
    for i in range(len(items)):
        if target_upper in items_upper[i]:
            found.append(items[i])
    return found


            
