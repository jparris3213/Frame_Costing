import tkinter as tk
from tkinter import ttk
import time


main = tk.Tk()

main.geometry("800x600")


#TODO: Declare Variables present on page, starting with Plywood

#TODO: Declare Functions for various Costing

def ply_data_collect():
    one_whole = int(qty_1_whole.get())
    one_partial = int(qty_1_partial.get())
    one_over = int(qty_1_over.get())
    five_whole = int(qty_5_whole.get())
    five_partial = int(qty_5_partial.get())
    five_over = int(qty_5_over.get())
    ten_whole = int(qty_10_whole.get())
    ten_partial = int(qty_10_partial.get())
    ten_over = int(qty_10_over.get())

    one_yield = ply_yield_func(one_whole,one_partial,one_over,1)
    five_yield = ply_yield_func(five_whole, five_partial, five_over, 5)
    ten_yield = ply_yield_func(ten_whole, ten_partial, ten_over, 10)

    average_yield = (one_yield + five_yield + ten_yield) / 3

    footage = (1 / average_yield) * 32
    ply_yield_label.configure(text = footage)
    

def ply_yield_func(whole,fraction,direction,qty):
    if direction == 96:
        sheets = whole + (fraction / direction)
        ply_yield = qty / sheets
        return ply_yield
    elif direction == 48:
        sheets = whole + ((48 - fraction) / direction)
        ply_yield = qty / sheets
        return ply_yield


#TODO: Admin Area: Number, Name, Customer, Current Price, New Price, MATLAB

#TODO: Plywood Yield Calculator

plywood_header_1 = tk.Label(text = "Qty")
plywood_header_2 = tk.Label(text = "Whole Sheets")
plywood_header_3 = tk.Label(text = "Partial Sheets")
plywood_header_4 = tk.Label(text = "/96 or /48")

qty_1_label = tk.Label(text = "One")
qty_1_whole = tk.Entry()
qty_1_partial = tk.Entry()
qty_1_over = tk.Entry()

qty_5_label = tk.Label(text = "Five")
qty_5_whole = tk.Entry()
qty_5_partial = tk.Entry()
qty_5_over = tk.Entry()

qty_10_label = tk.Label(text = "Ten")
qty_10_whole = tk.Entry()
qty_10_partial = tk.Entry()
qty_10_over = tk.Entry()

ply_yield_label = tk.Label(text = "0")
ply_yield_button = tk.Button( main, text = "Calc" , command = ply_data_collect)

#TODO: Hardwood Entry Table

#TODO: Labor Entry

#TODO: Spring Up Information Box

#TODO: Varibles for: Plywood, Hardwood, KD/Assembled

#TODO: Create layout manager for grid layout in tkinter

plywood_header_1.grid(row = 0 , column = 0)
plywood_header_2.grid(row = 0 , column = 1)
plywood_header_3.grid(row = 0 , column = 2)
plywood_header_4.grid(row = 0 , column = 3)

qty_1_label.grid(row = 1, column = 0)
qty_1_whole.grid(row = 1, column = 1)
qty_1_partial.grid(row = 1, column = 2)
qty_1_over.grid(row = 1, column =3)

qty_5_label.grid(row = 2, column = 0)
qty_5_whole.grid(row = 2, column = 1)
qty_5_partial.grid(row = 2, column = 2)
qty_5_over.grid(row = 2, column = 3)

qty_10_label.grid(row = 3, column = 0)
qty_10_whole.grid(row = 3, column = 1)
qty_10_partial.grid(row = 3, column = 2)
qty_10_over.grid(row = 3, column = 3)

ply_yield_label.grid(row = 4, column = 2)
ply_yield_button.grid(row = 4, column = 3)

main.mainloop()