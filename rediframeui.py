import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox

#Main Window and Label'ed Frames
main = tk.Tk()

main.geometry("900x600")

admin_LabelFrame = tk.LabelFrame(text = "Frame Info")
hardwood_LabelFrame = tk.LabelFrame(text = "Hardwood Info")
plywood_calc_LabelFrame = tk.LabelFrame(main, text = "Plywood Nest")

messagebox.showinfo(title="Redi-Frame Inc. Alpha v 0.1", message="Welcome to Redi Frame Software \n v 0.01 \n by Jacob Parris")

#TODO: Declare Functions for various Costing Procedures

#Plywood Calculator Functions

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
    ply_yield_label.configure(text = "Footage: " + str(round(footage,2)))
    ply_price = footage * .83
    ply_yield_cost.configure(text = "Cost of Ply: $" + str(round(ply_price,2)))
    

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

style_number_label = tk.Label(admin_LabelFrame, text = "Style Number")
style_name_label = tk.Label(admin_LabelFrame, text = "Style Name")
style_type_label = tk.Label(admin_LabelFrame, text = "Style Type")
delivery_type_label = tk.Label(admin_LabelFrame, text = "Delivery Method")
customer_name_label = tk.Label(admin_LabelFrame, text = "Customer")
style_number_entry = tk.Entry(admin_LabelFrame)
style_name_entry = tk.Entry(admin_LabelFrame)
style_type_entry = tk.Entry(admin_LabelFrame)
delivery_type_entry = tk.Entry(admin_LabelFrame)
customer_name_entry = tk.Entry(admin_LabelFrame)

#TODO: Plywood Yield Calculator

plywood_header_1 = tk.Label(plywood_calc_LabelFrame, text = "Qty")
plywood_header_2 = tk.Label(plywood_calc_LabelFrame, text = "Whole Sheets")
plywood_header_3 = tk.Label(plywood_calc_LabelFrame, text = "Partial Sheets")
plywood_header_4 = tk.Label(plywood_calc_LabelFrame, text = "/96 or /48")

qty_1_label = tk.Label(plywood_calc_LabelFrame, text = "One")
qty_1_whole = tk.Entry(plywood_calc_LabelFrame, width = 5)
qty_1_partial = tk.Entry(plywood_calc_LabelFrame, width = 5)
qty_1_over = tk.Entry(plywood_calc_LabelFrame, width = 5)

qty_5_label = tk.Label(plywood_calc_LabelFrame, text = "Five")
qty_5_whole = tk.Entry(plywood_calc_LabelFrame, width = 5)
qty_5_partial = tk.Entry(plywood_calc_LabelFrame, width = 5)
qty_5_over = tk.Entry(plywood_calc_LabelFrame, width = 5)

qty_10_label = tk.Label(plywood_calc_LabelFrame, text = "Ten")
qty_10_whole = tk.Entry(plywood_calc_LabelFrame, width = 5)
qty_10_partial = tk.Entry(plywood_calc_LabelFrame, width = 5)
qty_10_over = tk.Entry(plywood_calc_LabelFrame, width = 5)

ply_yield_label = tk.Label(plywood_calc_LabelFrame, text = "Footage: 00.00")
ply_yield_cost = tk.Label(plywood_calc_LabelFrame, text = "Cost  of Ply: $00.00")
ply_yield_button = tk.Button(plywood_calc_LabelFrame,  text = "Calc" , command = ply_data_collect)

#TODO: Hardwood Entry Table

table_headings = [ "Qty", "Part Name", "Length", "Width", "Footage", "With Waste", "Total", "Cost", "First Clip", "Remaining Clips","Edge/Face","Bandsaw?","Qty"]

table_headings_start = 0

for name in table_headings:
    table_headings = tk.Label(hardwood_LabelFrame, text = name)

    table_headings.grid(row = 0, column = table_headings_start)
    table_headings_start = table_headings_start + 1

for i in range(5):
    for n in range(12):
        table_entry = tk.Entry(hardwood_LabelFrame, width = 10)
        table_entry.grid(row = i + 1, column = n)

#TODO: Labor Entry

#TODO: Spring Up Information Box

#TODO: Varibles for: Plywood, Hardwood, KD/Assembled

#TODO: Create layout manager for grid layout in tkinter

#Label Frame Grid

admin_LabelFrame.grid(row = 0, column = 0)
plywood_calc_LabelFrame.grid(row = 0, column = 1)
hardwood_LabelFrame.grid(row = 1, column = 0, columnspan = 12)


#Admin Grid Locations (Within admin_LabelFrame)
style_number_label.grid(row = 0, column = 0)
style_name_label.grid(row = 1, column = 0)
style_type_label.grid(row = 2, column = 0)
delivery_type_label.grid(row = 3, column = 0)
customer_name_label.grid(row = 4, column = 0)

style_number_entry.grid(row = 0, column = 1)
style_name_entry.grid(row = 1, column = 1)
style_type_entry.grid(row = 2, column = 1)
delivery_type_entry.grid(row = 3, column = 1)
customer_name_entry.grid(row = 4, column = 1)


#Plywood Grid Locations (Within plywood_calc_LabelFrame)
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

ply_yield_label.grid(row = 4, column = 1)
ply_yield_cost.grid(row = 4, column = 2)
ply_yield_button.grid(row = 4, column = 3)

main.mainloop()