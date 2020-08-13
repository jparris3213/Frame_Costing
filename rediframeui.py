import tkinter as tk
from tkinter import ttk
import time


main = tk.Tk()

main.geometry("800x600")


#TODO: Declare Variables present on page, starting with Plywood

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

main.mainloop()