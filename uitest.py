import tkinter as tk
import time

def display_stuff():
    label.configure(text = entry.get())

window = tk.Tk()
label = tk.Label(text = "Test")
label.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button( window, text="Push Me!", command = display_stuff )
button.pack()

window.mainloop()
