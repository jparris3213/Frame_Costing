import tkinter as tk

def display_stuff():
    print("Hello World!")

window = tk.Tk()
label = tk.Label(text="Python rocks!")
entry = tk.Entry(text="Whats up?")
button = tk.Button( window, text="Push Me!", command = display_stuff )
label.pack()
entry.pack()
button.pack()

window.mainloop()
