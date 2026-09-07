## Imports
from tkinter import *
from tkinter import messagebox
from is_pos import is_positive_float

## Main Program
# Functions
def pounds_to_euros():
    pounds = txt_pounds.get()
    if is_positive_float(pounds):    
        euros = float(pounds) * 1.16
        txt_euros.insert(END, f"{euros:.2f}")
    else:
        messagebox.showerror("Error", "Please enter a number greater than 0")
window = Tk()
window.geometry("200x300")

LBL_pounds = Label(window, text = "Pounds")
LBL_pounds.pack()

txt_pounds = Entry(window, width = 15)
txt_pounds.pack()

btn_convert = Button(window, text = "Convert", command = pounds_to_euros)
btn_convert.pack(pady = 10)

LBL_euros = Label(window, text = "Euros")
LBL_euros.pack()

txt_euros = Entry(window, width = 15)
txt_euros.pack()

# Displays window
window.mainloop

