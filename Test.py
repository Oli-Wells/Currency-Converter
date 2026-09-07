## Imports
from tkinter import *

## Main Program
# Functions
def currency_input():
    counter = 1
    for currencies in currency_list:
        print("".format())

window = Tk()
window.geometry("200x300")

LBL_pounds = Label(window, text = "Pounds")
LBL_pounds.pack()

txt_pounds = Entry(window, width = 15)
txt_pounds.pack()

btn_convert = Button(window, text = "Convert")
btn_convert.pack(pady = 10)

LBL_euros = Label(window, text = "Euros")
LBL_euros.pack()

txt_euros = Entry(window, width = 15)
txt_euros.pack()

# Displays window
window.mainloop

