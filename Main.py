# import tkinter module 
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import requests
import json

data_retrieved = False

"""
Notes:
Maybe save the JSON into an external txt file. Then it can be accessed globally?
"""

def get_data(searchfield, qtyfield):
    url = "https://rapidapi.p.rapidapi.com/api/nutrition-data"

    searchfield = str(qtyfield.get()+ searchfield.get())
    querystring = {"ingr": (searchfield)}

    headers = {
        'x-rapidapi-key': "f249f2852bmshb6c60cd7bf5ce30p13225fjsn093a82d68c86",
        'x-rapidapi-host': "edamam-edamam-nutrition-analysis.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    global parsed
    parsed = json.loads(response.text)

    data_retrieved = True

    print(json.dumps(parsed, indent=4))
    

# Creating main tkinter window/toplevel 
master = Tk() 
master.geometry("400x400")
master.title("Nutri")
master.iconbitmap("Images\Smallicon.ico")

# Entry widgets, used to take entry from user 
searchfield = Entry(master, width = 40)
searchfield.grid(row = 0, column = 1, pady = 2, columnspan = 2) 


# Qty label
qtylabel = Label(master, text = "Qty: ")
qtylabel.grid(row = 1, column = 1, pady = 2, sticky = W)
# Qty entry 
qtyfield = Entry(master, width = 5, text = "1")
qtyfield.grid(row = 1, column = 1) 


# Search button
#searchfield = str(searchfield.get())
searchbutton = Button(master, text = "Search", command= lambda: get_data(searchfield, qtyfield))
searchbutton.grid(row = 1, column = 2, sticky = E)

path = "Images/Normal_logo.jpg"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(master, image = img)
panel.grid(row = 0, column = 0, sticky = W, pady = 2, rowspan = 2)



# Nutrition grid

# Key nutrition title
titlelabel = Label(master, text = "KEY NUTRITIONAL INFO")
titlelabel.config(font=("consolas", 15))
titlelabel.grid(row = 2, column = 0, columnspan = 2, sticky = W, pady = (30,10))

# Kcal label
kcallabel = Label(master, text = "Calories: ")
kcallabel.grid(row = 3, column = 0, columnspan = 2, sticky = W)

# Fat label
fatlabel = Label(master, text = "Fat: ")
fatlabel.grid(row = 4, column = 0, columnspan = 2, sticky = W)

# Saturates label
saturateslabel = Label(master, text = "Saturates: ")
saturateslabel.grid(row = 5, column = 0, columnspan = 2, sticky = W)

# Carbs label
carbslabel = Label(master, text = "Carbs: ")
carbslabel.grid(row = 6, column = 0, columnspan = 2, sticky = W)

# Sugar label
sugarlabel = Label(master, text = "Sugar: ")
sugarlabel.grid(row = 7, column = 0, columnspan = 2, sticky = W)
# Sugar data
sugardata = Label(master, text = "Test")
sugardata.grid(row = 7, column = 1, columnspan = 2, sticky = W)

""" # Kcal data
kcallabel = Label(master, text = "Kcal: ")
kcallabel.config(font=("consolas", 12))
kcallabel.grid(row = 3, column = 0, columnspan = 2, sticky = W)
 """

x=0
while data_retrieved == True:
    while x == 0:
        """ calories = str(parsed["calories"])
        print(calories)
        x = 1 """
        print("test")

mainloop() 

