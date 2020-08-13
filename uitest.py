import tkinter as tk
import time

def display_stuff():
    label.configure(text = entry.get())

window = tk.Tk()
window.geometry("800x600")
label = tk.Label(text = "Test")
label.grid(row = 0, column = 1)

entry = tk.Entry()
entry.grid(row = 0, column = 2)

button = tk.Button( window, text="Push Me!", command = display_stuff )
button.grid(row = 0, column = 3)

window.mainloop()
