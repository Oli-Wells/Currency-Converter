## Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from is_pos import is_positive_float

## File Handling
currency_csv = open("currency_list.csv", "r")
currency_list = currency_csv.read()
currency_list = currency_list.split(",")
currency_csv.close()

## Main Program
# Functions
def get_multiplier():
    return 1.16

def currency_conversion(multiplier):
    currency1 = txt_opt1.get()
    if is_positive_float(currency1):    
        currency2 = float(currency1) * multiplier
        txt_opt2.insert(END, f"{currency2:.2f}")
    else:
        messagebox.showerror("Error", "Please enter a number greater than 0")

# Base window
window = Tk()
window.geometry("200x300")

# Option 1 combobox
cb1 = ttk.Combobox(window, values=currency_list)
cb1.set("Select a currency")
cb1.pack()

# Currency Boxes

txt_opt1 = Entry(window, width = 15)
txt_opt1.pack()

multiplier = get_multiplier()

btn_convert = Button(window, text = "Convert", command = currency_conversion(multiplier))
btn_convert.pack(pady = 10)

# Option 2 dropdown
cb2 = ttk.Combobox(window, values=currency_list)
cb2.set("Select a currency")
cb2.pack()

txt_opt2 = Entry(window, width = 15)
txt_opt2.pack()

# Displays window
window.mainloop

