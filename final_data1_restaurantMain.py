import pickle

###################### STALL DETAILS ###########################

#category: H = Halal, NH = Not Halal
#location: r = restaurant, fc = foodcourt
#wait_nonpeak and wait_peak are in minutes

'''RestMain format:[restaurant_name][category/description/location]
         or [restaurant_name][date][Mon/Tue/Wed/Thu/Fri/Sat/Sun][0/1]
                                           (0 for opening time, 1 for closing time)'''
'''./menus/mac format: [mac_fries][price or day or time]'''


######-----------------1.McDonalds-------------------------########

mac_OC = {'Mon' : [600,2359],
          'Tue' : [600,2359],
          'Wed' : [600,2359],
          'Thu' : [600,2359],
          'Fri' : [600,2359],
          'Sat' : [600,2200],
          'Sun' : [600,2200]
          }

mac_main = {'date'          : mac_OC ,
            'category'      : 'H',
            'description'   : 'McDonald\'s predominantly sells hamburgers, various types of chicken, chicken sandwiches, French fries, soft drinks, breakfast items, and desserts. Products are offered as either "dine-in" or "take-out".' ,
            'location'      : 'r' ,
            'wait_nonpeak'  : 1,
            'wait_peak'     : 3.0
            }


######-----------------2.Miniwok-------------------------########

miniwok_OC = {'Mon' : [900,2000],
              'Tue' : [900,2000],
              'Wed' : [900,2000],
              'Thu' : [900,2000],
              'Fri' : [900,2000],
              'Sat' : [1100,1700],
              'Sun': [0000, 0000]
              }

miniwok_main = {'date'          : miniwok_OC ,
                'category'      : 'A',
                'description'   : 'Miniwok sells rice cooked with different meat and sauces, usually served with a generous helpinng of soy sauce. It is tasty, affordable and filling. A good experience especially on your cheat day!' , 
                'location'      : 'fc' ,
                'wait_nonpeak'  : 2,
                'wait_peak'     : 2.6
                }


######-----------------3.Mixrice-------------------------########

mixrice_OC = {'Mon' : [900,1900],
              'Tue' : [900,1900],
              'Wed' : [900,1900],
              'Thu' : [900,1900],
              'Fri' : [900,1900],
              'Sat' : [1100,1600],
              'Sun': [0000, 0000]
              }

mixrice_main = {'date'          : mixrice_OC ,
                'category'      : 'A',
                'description'   : 'It\'s prices are hard to predict but it will not fail to offer a myriad of options to choose from. Whether you want to eat vegetables or meat, mix rice has it all.',
                'location'      : 'fc',
                'wait_nonpeak'  : 1.5,
                'wait_peak'     : 2
                }

######-----------------4.Western-------------------------########

western_OC = {'Mon' : [900,2000],
              'Tue' : [900,2000],
              'Wed' : [900,2000],
              'Thu' : [900,2000],
              'Fri' : [900,2000],
              'Sat' : [1100,1700],
              'Sun': [0000, 0000]
              }

western_main = {'date'          : western_OC ,
                'category'      : 'H',
                'description'   : "If you want to feel like you are abroad, this stall is where you should go. It's fries are talked about all over NTU. The portions are huge and delicious.",
                'location'      : 'fc',
                'wait_nonpeak'  : 2,
                'wait_peak'     : 3.5
                }

#######-----------------5.KFC-------------------------########
 
kfc_OC = {'Mon' : [800,2200],
          'Tue' : [800,2200],
          'Wed' : [800,2200],
          'Thu' : [800,2200],
          'Fri' : [800,2359],
          'Sat': [900, 2359],
          'Sun' : [900,2100]
          }

kfc_main = {'date'          : kfc_OC ,
            'category'      : 'H',
            'description'   : "Finger Lickin' Good. This is how everyone definnes KFC. The fried chicken is amazing and the discount deals are very attractive. If you have a bad day, their mashed potatoes will make you feel amazing.",
            'location'      : 'r',
            'wait_nonpeak'  : 2,
            'wait_peak'     : 4.0
            }

######-----------------6.Subway-------------------------########

sub_OC = {'Mon' : [900,2200],
          'Tue' : [900,2200],
          'Wed' : [900,2200],
          'Thu' : [900,2200],
          'Fri' : [900,2200],
          'Sat' : [800,2200],
          'Sun' : [800,2100]
          }

sub_main = {'date'          : sub_OC ,
            'category'      : 'H',
            'description'   : 'SUBWAY is the largest submarine sandwich chain with more than 44,000 locations around the world. It is the perfect choice for people seeking quick, nutritious meals that the whole family can enjoy.',
            'location'      : 'r',
            'wait_nonpeak'  : 2,
            'wait_peak'     : 5
            }
            
#######-----------------7.Umi Sushi-------------------------########

umi_OC = {'Mon' : [900,2200],
          'Tue' : [900,2200],
          'Wed' : [900,2200],
          'Thu' : [900,2200],
          'Fri' : [900,2200],
          'Sat' : [800,2200],
          'Sun' : [800,2100]
          }

umi_main = {'date'          : umi_OC ,
            'category'      : 'A',
            'description'   : 'UmiSushi prepares and serves one of the freshest sushi in town at affordable prices. Besides sushi, we offer sashimi, bentos, udons and Japanese salads, enjoyed by customers of all ages and walks of life.',
            'location'      : 'r',
            'wait_nonpeak'  : 1.5,
            'wait_peak'     : 4
            }

######-------------------8.Vegetarian---------------------########

veg_OC      = {'Mon' : [900,1900],
              'Tue' : [900,1900],
              'Wed' : [900,1900],
              'Thu' : [900,1900],
              'Fri' : [900,1900],
              'Sat' : [1100,1700],
              'Sun': [0000, 0000]
              }

veg_main     = {'date'          : veg_OC ,
                'category'      : 'H',
                'description'   : 'The vegetarian store offers plenty of healthy and delicious options at an affordable price. Especially for vegetarians who have very few options, this is the stall to go!',
                'location'      : 'fc',
                'wait_nonpeak'  : 1.5,
                'wait_peak'     : 1.8
                }


######-----------------9.SOUP SPOON-------------------------########

soup_OC = {'Mon' : [900,2059],
          'Tue' : [900,2059],
          'Wed' : [600,2059],
          'Thu' : [800,2000],
          'Fri' : [900,2100],
          'Sat' : [900,2200],
          'Sun' : [1000,2200]
          }

soup_main = {'date'          : soup_OC ,
            'category'      : 'H',
            'description'   : 'They travel the world, discovering its cultures, one bowl of soup at a time. They are inspired by the incredible variety of this simple dish and they are passionate about turning ideas from around the world into recipes for homely moments.' ,
            'location'      : 'r' ,
            'wait_nonpeak'  : 1,
            'wait_peak'     : 2.0
            }


######-----------------10.MALAY-------------------------########

malay_OC = {'Mon': [900, 1900],
            'Tue': [900, 1900],
            'Wed': [900, 1900],
            'Thu': [900, 1900],
            'Fri': [900, 1900],
            'Sat': [1100, 1900],
            'Sun': [0000, 0000]
          }
malay_main = {'date': malay_OC,
            'category': 'H',
            'description': 'The Malay store offers various local dishes that will be sure to satisfy your cravings for local comfort food. From the variety of noodles to filling rice dishes, there will sure be a choice for you! ',
            'location': 'fc',
            'wait_nonpeak': 1.0,
            'wait_peak': 1.5
            }
######-----------------11.CHICKEN RICE-------------------------########

chick_OC = {'Mon': [900, 2000],
            'Tue': [900, 2000],
            'Wed': [900, 2000],
            'Thu': [900, 2000],
            'Fri': [900, 1900],
            'Sat': [1100, 1700],
            'Sun': [0000, 0000]
          }
chick_main = {'date': chick_OC,
              'category': 'H',
              'description': 'Who knew there are various types of Chicken Rice/Noddles? How does one elevate the already flavourful dish?! Stop by the Chicken Rice stall to taste all the delicious types that they have to offer! ',
              'location': 'fc',
              'wait_nonpeak': 1.0,
              'wait_peak': 1.5
              }


############################################COMBINED DICTIONARY################################################
restaurant_main = {'McDonald\'s'   : mac_main,
                   'Miniwok'     : miniwok_main,
                   'KFC'         : kfc_main,
                   'Subway'      : sub_main,
                   'Umisushi'    : umi_main,
                   'Mixrice'     : mixrice_main,
                   'Western'     : western_main,
                   'Vegetarian'  : veg_main,
                   'Malay'       : malay_main,
                   'Chicken Rice': chick_main,
                   'Soup Spoon'  : soup_main
                   }



#DUMPING
file_name = "./folder_data/RestMain"
fileObject = open(file_name,"wb")
pickle.dump(restaurant_main,fileObject)
fileObject.close()
###END###
