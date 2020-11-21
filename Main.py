# import tkinter module 
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import requests
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.graphics import renderPDF
import os
import numpy as np
import matplotlib.pyplot as plt


# region === Generate PDF ===

def generate_pdf(calories, Fat, Saturates, Carbs, Sugar, Fiber, Protein, Cholesterol, Sodium, Water, searchfield, weightfield):
    
    plt.clf()
    # dataset
    stringdata = [Fat, Saturates, Carbs, Sugar, Fiber, Protein]
    height = []

    for item in stringdata:
        item = item[:-1]
        item = int(item)
        height.append(item)

    

    bars = ('Fat', 'Saturates', 'Carbs', 'Sugar', 'Fiber', 'Protein')
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height)
    
    # Create names on the x-axis
    plt.xticks(y_pos, bars)

    plt.savefig('nutrition_graph.png')

    
    pdf = canvas.Canvas("Nutri_Report.pdf")

    image = ("Images/Normal_logo.jpg")
    pdf.drawImage(image, 50,720, width=70,height=70)

    graph = ("nutrition_graph.png")
    pdf.drawImage(graph, 100, 100, width=384,height=288)

    pdf.drawString(150, 760, "Nutri")
    pdf.drawString(150, 745, "Nutrition report for " + weightfield.get() + "g of " + searchfield.get())

    pdf.drawString(50, 680, "Total calories (Kcal): " + str(calories))

    pdf.drawString(50, 625, "Fat (g): " + str(Fat))
    pdf.drawString(50, 600, "Saturates (g): " + str(Saturates))
    pdf.drawString(50, 575, "Carbs (g): " + str(Carbs))
    pdf.drawString(50, 550, "Sugar (g): " + str(Sugar))
    pdf.drawString(50, 525, "Fiber (g): " + str(Fiber))

    pdf.drawString(300, 625, "Protein (g): " + str(Protein))
    pdf.drawString(300, 600, "Cholesterol (mg): " + str(Cholesterol))
    pdf.drawString(300, 575, "Sodium (mg): " + str(Sodium))
    pdf.drawString(300, 550, "Water (g): " + str(Water))


    #pdf.drawString(50, 500, r5c1 + "     " + r5c2)

    pdf.setTitle("Nutri report")

    pdf.save()
#endregion

# Nutrition grid data # 

def nutrition_data(searchfield, weightfield):
    data_file = open('Data.txt', 'r')
    raw_data = data_file.read()
    data_file.close()

    raw_data = json.loads(raw_data)

    #region   === Update labels ===
    # Calorie data
    calories = raw_data['calories']
    kcaldata.config(text= calories)

    # Fat data
    Fat = (str(round(int(raw_data['totalNutrients']['FAT']['quantity']), 4))) + "g"
    fatdata.config(text = Fat)

    # Saturates data
    Saturates = (str(round(int(raw_data['totalNutrients']['FASAT']['quantity']), 4))) + "g"
    saturatesdata.config(text = Saturates)

    # Carbs data
    Carbs = (str(round(int(raw_data['totalNutrients']['CHOCDF']['quantity']), 4))) + "g"
    carbdata.config(text = Carbs)

    # Sugar data
    Sugar = (str(round(int(raw_data['totalNutrients']['SUGAR']['quantity']), 4))) + "g"
    sugardata.config(text = Sugar)

    # Fiber data
    Fiber = (str(round(int(raw_data['totalNutrients']['FIBTG']['quantity']), 4))) + "g"
    fiberdata.config(text = Fiber)

    # Protein data
    Protein = (str(round(int(raw_data['totalNutrients']['PROCNT']['quantity']), 4))) + "g"
    proteindata.config(text = Protein)

    # Cholesterol data
    Cholesterol = (str(round(int(raw_data['totalNutrients']['CHOLE']['quantity']), 4))) + "mg"
    cholesteroldata.config(text = Cholesterol)

    # Sodium data
    Sodium = (str(round(int(raw_data['totalNutrients']['NA']['quantity']), 4))) + "mg"
    sodiumdata.config(text = Sodium)

    # Water data
    Water = (str(round(int(raw_data['totalNutrients']['WATER']['quantity']), 4))) + "g"
    waterdata.config(text = Water)

    generate_pdf(calories, Fat, Saturates, Carbs, Sugar, Fiber, Protein, Cholesterol, Sodium, Water, searchfield, weightfield)


    #endregion


def get_data(searchfield, weightfield):
    url = "https://rapidapi.p.rapidapi.com/api/nutrition-data"

    final_query = str(searchfield.get() + " " + weightfield.get() + "g")
    querystring = {"ingr": (final_query)}

    headers = {
        'x-rapidapi-key': "f249f2852bmshb6c60cd7bf5ce30p13225fjsn093a82d68c86",
        'x-rapidapi-host': "edamam-edamam-nutrition-analysis.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    parsed = json.loads(response.text)

    data_file = open('Data.txt', 'w')
    data_file.write(str(json.dumps(parsed, indent=4)))
    data_file.close()

    nutrition_data(searchfield, weightfield)
    

# Creating main tkinter window/toplevel 
master = Tk() 
master.geometry("360x350")
master.title("Nutri")
master.iconbitmap("Images\Smallicon.ico")

# Item label
itemlabel = Label(master, text = "Item")
itemlabel.grid(row = 0, column = 1, sticky = W)
# Item entry 
searchfield = Entry(master, width = 20)
searchfield.grid(row = 1, column = 1, columnspan = 1, sticky = W, pady = (0, 10)) 

# Weight label
weightlabel = Label(master, text = "Weight (g):")
weightlabel.grid(row = 2, column = 1, pady = 2, sticky = W)
# Weight entry 
weightfield = Entry(master, width = 5)
weightfield.grid(row = 2, column = 1, sticky = E) 

# Search button
searchbutton = Button(master, text = "Search", command= lambda: get_data(searchfield, weightfield), width = 10)
searchbutton.grid(row = 1, column = 2, columnspan = 1, sticky = E, pady = (0, 10), padx = (20, 0))

path = "Images/Normal_logo.jpg"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(master, image = img)
panel.grid(row = 0, column = 0, sticky = W, pady = 2, rowspan = 3)


#region === Nutrition grid labels ===

# Key nutrition title
titlelabel = Label(master, text = "KEY NUTRITIONAL INFO")
titlelabel.config(font=("consolas", 15))
titlelabel.grid(row = 3, column = 0, columnspan = 2, sticky = W, pady = (30,5))

# Calorie label
kcallabel = Label(master, text = "Calories: ")
kcallabel.grid(row = 4, column = 0, columnspan = 2, sticky = W)
# Calorie data
kcaldata = Label(master, text = "")
kcaldata.grid(row = 4, column = 1, columnspan = 2, sticky = W)

# Fat label
fatlabel = Label(master, text = "Fat: ")
fatlabel.grid(row = 5, column = 0, columnspan = 2, sticky = W)
# Fat data
fatdata = Label(master, text = "")
fatdata.grid(row = 5, column = 1, columnspan = 2, sticky = W)

# Saturates label
saturateslabel = Label(master, text = "Saturates: ")
saturateslabel.grid(row = 6, column = 0, columnspan = 2, sticky = W)
# Saturates data
saturatesdata = Label(master, text = "")
saturatesdata.grid(row = 6, column = 1, columnspan = 2, sticky = W)

# Carbs label
carbslabel = Label(master, text = "Carbs: ")
carbslabel.grid(row = 7, column = 0, columnspan = 2, sticky = W)
# Carbs data
carbdata = Label(master, text = "")
carbdata.grid(row = 7, column = 1, columnspan = 2, sticky = W)

# Sugar label
sugarlabel = Label(master, text = "Sugar: ")
sugarlabel.grid(row = 8, column = 0, columnspan = 2, sticky = W)
# Sugar data
sugardata = Label(master, text = "")
sugardata.grid(row = 8, column = 1, columnspan = 2, sticky = W)

# Fiber label
fiberlabel = Label(master, text = "Fiber: ")
fiberlabel.grid(row = 4, column = 2, columnspan = 2, sticky = W)
# Fiber data
fiberdata = Label(master, text = "")
fiberdata.grid(row = 4, column = 3, columnspan = 2, sticky = W)

# Protein label
proteinlabel = Label(master, text = "Protein: ")
proteinlabel.grid(row = 5, column = 2, columnspan = 2, sticky = W)
# Protein data
proteindata = Label(master, text = "")
proteindata.grid(row = 5, column = 3, columnspan = 2, sticky = W)

# Cholesterol label
cholesterollabel = Label(master, text = "Cholesterol: ")
cholesterollabel.grid(row = 6, column = 2, columnspan = 2, sticky = W)
# Cholesterol data
cholesteroldata = Label(master, text = "")
cholesteroldata.grid(row = 6, column = 3, columnspan = 2, sticky = W)

# Sodium label
sodiumlabel = Label(master, text = "Sodium: ")
sodiumlabel.grid(row = 7, column = 2, columnspan = 2, sticky = W)
# Sodium data
sodiumdata = Label(master, text = "")
sodiumdata.grid(row = 7, column = 3, columnspan = 2, sticky = W)

# Water label
waterlabel = Label(master, text = "Water: ")
waterlabel.grid(row = 8, column = 2, columnspan = 2, sticky = W)
# Water data
waterdata = Label(master, text = "")
waterdata.grid(row = 8, column = 3, columnspan = 2, sticky = W)
#endregion

#region === Generate PDF ===
# Generate pdf button
def open_pdf():
    os.startfile("Nutri_Report.pdf")
pdfbutton = Button(master, text = "Generate PDF", command= open_pdf, width = 15)
pdfbutton.grid(row = 9, column = 0, pady = (30, 0), sticky = W)



#endregion

mainloop() 