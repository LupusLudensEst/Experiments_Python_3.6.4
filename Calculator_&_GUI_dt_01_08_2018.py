# Calculator_&_GUI_dt_01_08_2018

"""
Algorithm
1. Import needed library
2. Create window
3. Create all buttons
4 Create calculator itself
    a) Exclude opportinity entering of letters into calculator
    b) Addition opportunity of counting(main part of this program)
    c) Addition of button "clean"
"""

# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
#
# root = Tk()
# root.title("Gurov's Calculator")
#
# # Calculator logic writting
# def calc(key):
#     global memory
#     if key == "=":
#
# # Excluding letters writting
#         str1 = "0123456789-+*/."
#         if calc_entry.get()[0] not in str1:
#             calc_entry.insert(END, "First symbol is not a number!")
#             messagebox.showerror("Mistype, you entered not a number!")
#
# # Counting
#         try:
#             result = eval(calc_entry.get())
#             calc_entry.insert(END, "=" + str(result))
#         except:
#             calc_entry.insert(END, "Mistake!")
#             messagebox.showerror("Mistake! Check what you entered!")
#
# # Clean the field
#     elif key == "C":
#         calc_entry.delete(0, END)
#
# # Change -+
#     elif key == "-/+":
#         if "=" in calc_entry.get():
#             calc_entry.delete(0, END)
#         try:
#             if calc_entry.get()[0] == "-":
#                 calc_entry.delete(0)
#             else:
#                 calc_entry.insert(0, "-")
#         except IndexError:
#             pass
#     else:
#         if "=" in calc_entry.get():
#             calc_entry.delete(0, END)
#         calc_entry.insert(END, key)
#
#
# # Create all buttons
# buttons_list = [
#     "7", "8", "9", "+", "-",
#     "4", "5", "6", "*", "/",
#     "1", "2", "3", "-/+", "=",
#     "0", ".", "C", "", ""
#     ]
# r = 1
# c = 0
#
# for i in buttons_list:
#     rel = ""
#     cmd = lambda x = i: calc(x)
#     ttk.Button(root, text = i, command = cmd).grid(row = r, column = c)
#     c += 1
#     if c > 4:
#         c = 0
#         r += 1
#
# calc_entry = Entry(root, width = 33)
# calc_entry.grid(row = 0, column = 0, columnspan = 5)
#
# root.mainloop



from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import *

root = Tk()
root.title("Gurov's Calculator")


# Calculator logic writting
def calc(key):
    global memory
    if key == "=":

# Excluding letters writting
        str1 = "0123456789-+*/.()"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "   First symbol isn't a number!")
            messagebox.showerror(0, "Mistype, you entered not a number!")

# Counting
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "   Mistake!")
            messagebox.showerror(0, "Mistake! Check what you entered!")
        # if key == "√x":
            calc_entry.get = math.sqrt(calc_entry.insert)
        # if key == "x^2":
            calc_entry.get = calc_entry.insert ** 2    

# Clean the field
    elif key == "C":
        calc_entry.delete(0, END)

# Change -+
    elif key == "-/+":
        if "=" in ():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
        
       
# Create all buttons
buttons_list = [
    "7", "8", "9", "+", "-", 
    "4", "5", "6", "*", "/", 
    "1", "2", "3", "-/+", "=",
    "0", ".", "C", "(", ")",  # √x- math.sqrt # x^2- 3 ** 2 = 9
    ]
r = 1
c = 0

for i in buttons_list:
    rel = ""
    cmd = lambda x = i: calc(x)  
    ttk.Button(root, text = i, command = cmd).grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 50)
calc_entry.grid(row = 0, column = 0, columnspan = 5)
    
root.mainloop
