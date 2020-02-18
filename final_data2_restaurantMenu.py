import pickle
# 'veg' (0 for False, 1 for True)

##HOW TO CALL: [mac_fries][price or day or time]


###1.MAC
mac_burger = {'price': 3.5,
              'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
              'time': [1100, 2200],
              'type': 'Food',
              'veg': 0
              }

mac_fries = {'price': 3.0,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [600, 1800],
             'type': 'Sides',
             'veg': 1
             }

mac_nugget = {'price': 3.7,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [600, 2359],
             'type': 'Sides',
             'veg': 0
             }

mac_fish = {'price': 3.7,
             'day': ['Mon','Wed', 'Fri', 'Sat'],
             'time': [1200, 2359],
             'type': 'Food',
             'veg': 0
             }

mac_spicy = {'price': 4.0,
             'day': ['Mon', 'Tue', 'Wed', 'Thu'],
             'time': [600, 2359],
             'type': 'Sides',
             'veg': 0
             }

mac_hotcakes = {'price': 3.5,
             'day': ['Mon', 'Tue', 'Wed', 'Thu'],
             'time': [600, 1130],
             'type': 'Food',
             'veg': 1
             }
mac_bf = {'price': 5.8,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri' , 'Sat' , 'Sun'],
             'time': [600, 1200],
             'type': 'Food',
             'veg': 0
             }

mac_iced_latte = {'price': 5.5,
                  'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                  'time': [1200, 2200],
                  'type': 'Drinks',
                  'veg': 1
                  }

mac_hot_milo = {'price': 1.8,
                'day': ['Sat', 'Sun'],
                'time': [600, 2200],
                'type': 'Drinks',
                'veg': 1
                }
mac_coffee = {'price': 1.8,
             'day': ['Mon',  'Fri' , 'Sat' , 'Sun'],
             'time': [600, 1200],
             'type': 'Drinks',
             'veg': 1
             }

mac_menu = {'Burger': mac_burger,
            'Frenchfries': mac_fries,
            'McNuggets' : mac_nugget,
            'Fillet O Fish' : mac_fish,
            'McSpicy' : mac_spicy,
            'Hotcakes' : mac_hotcakes,
            'Breakfast Platter' : mac_bf,
            'Iced Latte': mac_iced_latte,
            'Hot Milo': mac_hot_milo,
            'Hot Coffee' : mac_coffee
            }
            

file_name = "./folder_data/menus/McDonald's"
fileObject = open(file_name,"wb")
pickle.dump(mac_menu,fileObject)
fileObject.close()



#2.MINIWOK
miniwok_chicken = {  'price'  : 7.5,
                'day'    : ['Mon','Tue','Wed','Thu','Fri','Sat'] ,
                'time'   : [1100,2200] ,
                'type'   : 'Food',
                'veg'    : 0
            }
            
miniwok_pork = {  'price'  : 5.0,
            'day'    : ['Mon','Tue','Wed','Thu','Fri',] ,
            'time'   : [600,1800] ,
            'type'   : 'Food',
            'veg'    : 0
            }
miniwok_beef = {  'price'  : 5.5,
            'day'    : ['Wed','Thu','Fri'] ,
            'time'   : [1200,2200] ,
            'type'   : 'Food',
            'veg'    : 0
            }
            

miniwok_menu = {'Chicken Wok' : miniwok_chicken,
            'Pork Wok' : miniwok_pork ,
            'Beef Wok' : miniwok_beef
            }
            
file_name = "./folder_data/menus/Miniwok"
fileObject = open(file_name,"wb")
pickle.dump(miniwok_menu,fileObject)
fileObject.close()


###3.KFC
kfc_chick = {'price': 2.5,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [1200, 2200],
             'type': 'Food',
             'veg': 0
             }

kfc_bucket = {'price': 14.5,
             'day': ['Fri', 'Sat', 'Sun'],
             'time': [1200, 2359],
             'type': 'Food',
             'veg': 0
             }

kfc_cheese = {'price': 2.5,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [800, 2200],
             'type': 'Sides',
             'veg': 1
             }

kfc_mash = {'price': 2.0,
             'day': ['Mon', 'Wed', 'Sat'],
             'time': [800, 2200],
             'type': 'Sides',
             'veg': 1
             }

kfc_porridge = {'price': 3.5,
             'day': ['Mon', 'Tue', 'Sat', 'Sun'],
             'time': [800, 1200],
             'type': 'Food',
             'veg': 0
             }

kfc_froyo = {'price': 2.5,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [800, 2359],
             'type': 'Dessert',
             'veg': 1
             }


kfc_wrap = {'price': 4.0,
            'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            'time': [800, 1200],
            'type': 'Food',
            'veg': 0
            }
kfc_sjora = {'price': 1.9,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [800, 2200],
             'type': 'Drinks',
             'veg': 1
             }

kfc_milo = {'price': 1.9,
             'day': [ 'Tue',  'Thu', 'Sat', 'Sun'],
             'time': [800, 2200],
             'type': 'Drinks',
             'veg': 1
             }

kfc_tea = {'price': 1.1,
           'day': ['Sat', 'Sun'],
           'time': [800, 1200],
           'type': 'Drinks',
           'veg': 1
           }

kfc_menu = {'Chicken': kfc_chick,
            'Bucket Chicken' : kfc_bucket,
            'Chicken Porridge' : kfc_porridge,
            'Breakfast Wrap': kfc_wrap,
            'Froyo' : kfc_froyo,
            'Sjora': kfc_sjora,
            'Cheese Fries' : kfc_cheese,
            'Mashed Potatoes' : kfc_mash,
            'Ice Milo' : kfc_milo,
            'Hot Tea': kfc_tea
            }
            
file_name = "./folder_data/menus/KFC"
fileObject = open(file_name,"wb")
pickle.dump(kfc_menu,fileObject)
fileObject.close()


###4.SUBWAY
sub_coffee = {'price': 1.5,
              'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
              'time': [900, 1200],
              'type': 'Drinks',
              'veg': 1
              }
sub_salad = {'price': 5.5,
             'day': ['Sat', 'Sun'],
             'time': [1200, 2200],
             'type': 'Food',
             'veg': 1
             }

sub_flatbread = {'price': 5.0,
             'day': ['Mon', 'Wed', 'Fri', 'Sat'],
             'time': [900, 2200],
             'type': 'Food',
             'veg': 0
             }

sub_melt = {'price': 5.2,
             'day': [ 'Tue' 'Wed', 'Fri', 'Sat'],
             'time': [1200, 2200],
             'type': 'Food',
             'veg': 0
             }
sub_chick = {'price': 4.2,
             'day': ['Mon', 'Tue' 'Wed', 'Sat' , 'Sun'],
             'time': [800, 2200],
             'type': 'Food',
             'veg': 0
             }

sub_cookie = {'price': 3.0,
             'day': ['Mon', 'Wed', 'Fri', 'Sat'],
             'time': [800, 1500],
             'type': 'Sides',
             'veg': 1
             }
sub_chips = {'price': 2.3,
             'day': ['Mon', 'Wed', 'Fri', 'Sat' , 'Sun'],
             'time': [1300, 2200],
             'type': 'Sides',
             'veg': 1
             }

sub_turkey = {'price': 5.3,
              'day': ['Wed', 'Thu', 'Fri', 'Sun'],
              'time': [800, 2200],
              'type': 'Food',
              'veg': 0
              }
sub_break = {'price': 6,
             'day': ['Mon', 'Fri', 'Sat', 'Sun'],
             'time': [800, 1200],
             'type': 'Food',
             'veg': 0
             }

sub_menu = {'Breakfast Wrap': sub_break,
            'Salad': sub_salad,
            'Flatbread' : sub_flatbread,
            'Cookie' : sub_cookie,
            'Chips' : sub_chips,
            'Subway Melt' : sub_melt,
            'Roasted Chicken Sub' : sub_chick,
            'Black Coffee': sub_coffee,
            'Turkey Sub': sub_turkey
            }

file_name = "./folder_data/menus/Subway"
fileObject = open(file_name,"wb")
pickle.dump(sub_menu,fileObject)
fileObject.close()


###5.UMISUSHI
umi_poke = {'price': 6.0,
            'day': ['Tue', 'Wed', 'Fri', 'Sat'],
            'time': [1200, 2000],
            'type': 'Food',
            'veg': 0
            }

umi_platter ={'price': 15.0,
            'day': ['Thu', 'Fri', 'Sat', 'Sun'],
            'time': [1700, 2200],
            'type': 'Food',
            'veg': 0
            }

umi_veg ={'price': 13.0,
            'day': ['Thu', 'Fri', 'Sat', 'Sun'],
            'time': [1700, 2200],
            'type': 'Food',
            'veg': 1
            }

umi_salad = {'price': 5.0,
            'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'time': [800, 2200],
            'type': 'Food',
            'veg': 1
            }


umi_bento = {'price': 4.7,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Sun'],
             'time': [900, 1700],
             'type': 'Food',
             'veg': 0
             }
umi_donburi = {'price': 6.2,
             'day': ['Mon', 'Tue', 'Thu',  'Sat'],
             'time': [900, 2200],
             'type': 'Food',
             'veg': 0
             }

umi_asahi = {'price': 3.2,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [1900, 2200],
             'type': 'Drinks',
             'veg': 1
             }
umi_coke = {'price': 1.8,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [800, 2200],
             'type': 'Drinks',
             'veg': 1
             }
umi_green = {'price': 2.2,
             'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
             'time': [900, 2200],
             'type': 'Drinks',
             'veg': 1
             }

umi_menu = {'Poke Bowl': umi_poke,
            'Sushi Platter' : umi_platter,
            'Veg Sushi Platter' : umi_veg,
            'Salad' : umi_salad,
            'Donburi' : umi_donburi,
            'Asahi' : umi_asahi,
            'Coke' : umi_coke,
            'Bento': umi_bento,
            'Green Tea': umi_green
            }
            
file_name = "./folder_data/menus/Umisushi"
fileObject = open(file_name,"wb")
pickle.dump(umi_menu,fileObject)
fileObject.close()

###6.MIX RICE
mixrice_chicken = { 'price'  : 1.3,
                    'day'    : ['Mon','Tue','Wed','Thu','Fri','Sat'] ,
                    'time'   : [900,1700] ,
                    'type'   : 'Meat',
                    'veg'    : 0
                    }
            
mixrice_vege = {    'price'  : 1.0,
                    'day'    : ['Mon','Tue','Wed','Thu','Fri',] ,
                    'time'   : [1200,1800] ,
                    'type'   : 'Vegetables',
                    'veg'    : 1
                    }
                    
mixrice_fish = {'price'  : 2.5,
                'day'    : ['Wed','Thu','Fri'] ,
                'time'   : [1500,1900] ,
                'type'   : 'Meat',
                'veg'    : 0
                }
mixrice_rice = {'price'  : 0.5,
                'day'    : ['Mon','Tue','Wed','Thu','Fri','Sat'] ,
                'time'   : [900,1900] ,
                'type'   : 'Grains',
                'veg'    : 1
                }
            

mixrice_menu = {'Rice' : mixrice_rice,
                'Fish' : mixrice_fish ,
                'Chicken' : mixrice_chicken ,
                'Vegetables' : mixrice_vege
                }

file_name = "./folder_data/menus/Mixrice"
fileObject = open(file_name,"wb")
pickle.dump(mixrice_menu,fileObject)
fileObject.close()

#7.WESTERN
western_chop = {  'price'  : 6.3,
                  'day'    : ['Mon','Tue','Wed','Thu','Fri','Sat'] ,
                  'time'   : [900,1900] ,
                  'type'   : 'Meat',
                  'veg'    : 0
                }
            
western_pasta = {   'price'  : 5.0,
                    'day'    : ['Mon','Tue','Wed','Thu','Fri',] ,
                    'time'   : [1200,1800] ,
                    'type'   : 'Pasta',
                    'veg'    : 1
                }
                
western_ribs = {'price'  : 2.5,
                'day'    : ['Wed','Thu','Fri'] ,
                'time'   : [1500,1900] ,
                'type'   : 'Meat',
                'veg'    : 0
                }

western_menu = {'Chop' : western_chop,
                'Ribs' : western_ribs ,
                'Pasta' : western_pasta ,
                }
                
file_name = "./folder_data/menus/Western"
fileObject = open(file_name,"wb")
pickle.dump(western_menu,fileObject)
fileObject.close()


###8.VEGETARIAN
veg_friedrice = {  'price'  : 0.8,
                'day'    : ['Mon','Tue','Wed','Thu','Fri'] ,
                'time'   : [900,1900] ,
                'type'   : 'Vegetables',
                'veg'    : 1
            }
            
veg_bokcoy = {  'price'  : 0.8,
            'day'    : ['Mon','Tue','Wed','Thu','Fri','Sat'] ,
            'time'   : [1200,1800] ,
            'type'   : 'Vegetables',
            'veg'    : 1
            }
            
veg_fakemeat = {  'price'  : 1.0,
            'day'    : ['Wed','Thu','Fri'] ,
            'time'   : [1500,1900] ,
            'type'   : 'Vegetables',
            'veg'    : 1
            }
            
veg_rice = {'price'  : 0.5,
            'day'    : ['Mon','Tue','Wed','Thu','Fri','Sat'] ,
            'time'   : [900,1900] ,
            'type'   : 'Grains',
            'veg'    : 1
            }

veg_menu = {'Rice' : veg_rice,
            'Fakemeat' : veg_fakemeat ,
            'Bokcoy' : veg_bokcoy ,
            'Friedrice' : veg_friedrice
            }

file_name = "./folder_data/menus/Vegetarian"
fileObject = open(file_name,"wb")
pickle.dump(veg_menu,fileObject)
fileObject.close()

###9.MALAY
malay_meesiam = {'price': 2.5,
                 'day': ['Mon', 'Tue', 'Wed' , 'Thu'],
                 'time': [900, 1700],
                 'type': 'Noodles',
                 'veg': 0
                 }

malay_meerebus = {'price': 2.5,
                  'day': ['Mon', 'Wed', 'Thu', 'Sat'],
                  'time': [900, 1700],
                  'type': 'Noodles',
                  'veg': 0
              }

malay_meesoto = {'price': 2.0,
                 'day': ['Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                 'time': [1200, 1900],
                 'type': 'Noodles',
                 'veg': 0
                }

malay_laksa = {'price': 2.6,
               'day': ['Mon' , 'Wed', 'Thu', 'Fri'],
               'time': [1200, 1900],
               'type': 'Noodles',
               'veg': 0
            }

malay_nasilemak = {'price': 3.0,
                   'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                   'time': [900, 1500],
                   'type': 'Rice',
                   'veg': 0
                   }

malay_vegfriedrice = {'price': 2.7,
                      'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                      'time': [900, 1900],
                      'type': 'Rice',
                      'veg': 1
                   }

malay_seafriedrice = {'price': 3.5,
                      'day': ['Tue', 'Wed', 'Thu', 'Fri'],
                      'time': [900, 1900],
                      'type': 'Rice',
                      'veg': 0
                   }

malay_plainrice = {'price': 0.7,
                   'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                   'time': [900, 1900],
                   'type': 'Rice',
                   'veg': 1
                   }


malay_satay = {'price': 0.8,
                'day': ['Wed', 'Thu', 'Fri', 'Sat'],
                'time': [1500, 1900],
                'type': 'Sides',
                'veg': 0
                   }

malay_nugget = {'price': 0.6,
                'day': ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                'time': [900, 1900],
                'type': 'Sides',
                'veg': 0
                   }

malay_menu = {'Mee Siam': malay_meesiam,
              'Mee Rebus': malay_meerebus,
              'Mee Soto': malay_meesoto,
              'Laksa': malay_laksa,
              'Nasi Lemak': malay_nasilemak,
              'Vegetarian Fried Rice': malay_vegfriedrice,
              'Seafood Fried Rice' : malay_seafriedrice,
              'Plain Rice': malay_plainrice,
              'Satay': malay_satay,
              'Nugget': malay_nugget
            }

file_name = "./folder_data/menus/Malay"
fileObject = open(file_name, "wb")
pickle.dump(malay_menu, fileObject)
fileObject.close()


###10.CHICKEN RICE
chick_roasted_r = {'price': 2.5,
                 'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                 'time': [900, 1900],
                 'type': 'Rice',
                 'veg': 0
                 }

chick_cutlet_r = {'price': 2.5,
                  'day': ['Thu', 'Fri', 'Sat'],
                  'time': [900, 1900],
                  'type': 'Rice',
                  'veg': 0
              }

chick_lemon_r = {'price': 2.0,
                 'day': ['Tue','Wed', 'Fri'],
                 'time': [1200, 1900],
                 'type': 'Rice',
                 'veg': 0
                }

chick_charsiew_r = {'price': 2.6,
               'day': ['Wed', 'Thu', 'Fri'],
               'time': [1200, 1900],
               'type': 'Rice',
               'veg': 0
            }

chick_roasted_n = {'price': 3.0,
                   'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                   'time': [900, 1900],
                   'type': 'Noodles',
                   'veg': 0
                   }

chick_charsiew_n = {'price': 2.7,
                      'day': ['Mon', 'Tue', 'Thu', 'Fri'],
                      'time': [1200, 1500],
                      'type': 'Noodles',
                      'veg': 0
                   }

chick_wanton = {'price': 3.5,
                      'day': ['Thu', 'Fri', 'Sat'],
                      'time': [900, 1900],
                      'type': 'Noodles',
                      'veg': 0
                   }

chick_curry = {'price': 0.7,
                   'day': ['Fri', 'Sat'],
                   'time': [900, 1900],
                   'type': 'Noodles',
                   'veg': 0
                   }
chick_mock = {'price': 0.7,
                   'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
                   'time': [900, 1900],
                   'type': 'Rice',
                   'veg': 1
                   }



chick_menu = { 'Classic Chicken Rice' : chick_roasted_r,
               'Chicken Cutlet Rice' : chick_cutlet_r,
               'Lemon Chicken Rice' : chick_lemon_r,
               'Char Siew Chicken Rice' : chick_charsiew_r,
               'Roasted Chicken Noodle' : chick_roasted_n,
               'Char Siew Chicken Noodle' : chick_charsiew_n,
               'Wanton Chicken Noddle' : chick_wanton,
               'Curry Chicken Noodle' : chick_curry,
               'Mock Chicken Rice' : chick_mock

            }
            
file_name = "./folder_data/menus/Chicken Rice"
fileObject = open(file_name, "wb")
pickle.dump(chick_menu, fileObject)
fileObject.close()


###11.SOUP SPOON
soups_sandwitch_set = {'price': 13.4,
                 'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                 'time': [900, 1200],
                 'type': 'Set Meal',
                 'veg': 0
                 }

soups_potpie_set = {'price': 12.8,
                 'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                 'time': [900, 1200],
                 'type': 'Set Meal',
                 'veg': 0
                 }

soups_redrice_set = {'price': 10.4,
                 'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
                 'time': [900, 2200],
                 'type': 'Set Meal',
                 'veg': 0
                 }

soups_tangytomato = {'price': 7.2,
               'day': ['Wed', 'Thu', 'Fri'],
               'time': [1000, 1900],
               'type': 'A La Carte',
               'veg': 1
            }

soups_roastedpump = {'price': 7.2,
               'day': ['Wed', 'Thu', 'Fri'],
               'time': [1000, 1900],
               'type': 'A La Carte',
               'veg': 1
            }

soups_meatlessminestrone = {'price': 7.7,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [1200, 1900],
               'type': 'A La Carte',
               'veg': 1
            }

soups_tokyochickenstew = {'price': 8.3,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [1200, 1900],
               'type': 'A La Carte',
               'veg': 0
            }

soups_sgchicken = {'price': 8.8,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [1000, 1900],
               'type': 'A La Carte',
               'veg': 0
            }
soups_beefgoulash = {'price': 9.4,
               'day': ['Mon', 'Tue', 'Wed', 'Thu'],
               'time': [1200, 1900],
               'type': 'A La Carte',
               'veg': 0
            }

soups_tunamayo = {'price': 5.8,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Sandwiches',
               'veg': 0
            }
            
soups_tomatocheese = {'price': 5.1,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Sandwiches',
               'veg': 1
            }

soups_teriyakichicken = {'price': 6.0,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Sandwiches',
               'veg': 0
            }

soups_falafel = {'price': 5.5,
               'day': ['Mon', 'Tue', 'Wed'],
               'time': [800, 1300],
               'type': 'Flat Breads',
               'veg': 1
            }

soups_bulgogibeef = {'price': 6.2,
               'day': ['Mon', 'Tue', 'Wed'],
               'time': [800, 1300],
               'type': 'Flat Breads',
               'veg': 0
            }

soups_herbchicken = {'price': 5.7,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Flat Breads',
               'veg': 0
            }

soups_caesar = {'price': 5.1,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Salads',
               'veg': 1
            }

soups_asiantoufu = {'price': 5.1,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Salads',
               'veg': 1
            }

soups_chilledsoba = {'price': 6.1,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Salads',
               'veg': 0
            }

soups_cranberry = {'price': 6.2,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat'],
               'time': [800, 1300],
               'type': 'Salads',
               'veg': 0
            }

soups_steamedcorn = {'price': 2.3,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat','Sun'],
               'time': [800, 2100],
               'type': 'Sides',
               'veg': 1
            }

soups_garlicky = {'price': 3.9,
               'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri','Sat','Sun'],
               'time': [800, 2100],
               'type': 'Sides',
               'veg': 1
            }


soups_menu = { 'Sandwich Set' : soups_sandwitch_set,
               'Salad Set' : soups_potpie_set,
               'Red Rice Set' : soups_redrice_set,
               'Tangy Tomato with Basil' : soups_tangytomato,
               'Roasted Pumpkin' : soups_roastedpump,
               'Meatless Minestrone' : soups_meatlessminestrone,
               'Tokyo Chicken Stew' : soups_tokyochickenstew,
               'SG Chicken & Mushroom Ragout' : soups_sgchicken,
               'Beef Goulash' : soups_beefgoulash,
               'Tuna Mayo' : soups_tunamayo,
               'Tomato Cheese Toastie' : soups_tomatocheese,
               'Teriyaki Chicken' : soups_teriyakichicken,
               'Falafel with Hummus & Mint' : soups_falafel,
               'Bulgogi Beef with Quinoa' : soups_bulgogibeef,
               'Herb Chicken Breast' : soups_herbchicken,
               'Caesar Salad' : soups_caesar,
               'Asian Tofu Salad' : soups_asiantoufu,
               'Chilled Soba' : soups_chilledsoba,
               'Cranberry Chicken Fusilli Salad' : soups_cranberry,
               'Steamed Corn' : soups_steamedcorn,
               'Garlicky Focaccia' : soups_garlicky
            }
            
file_name = "./folder_data/menus/Soup Spoon"
fileObject = open(file_name, "wb")
pickle.dump(soups_menu, fileObject)
fileObject.close()
