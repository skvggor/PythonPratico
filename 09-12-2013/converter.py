# example from section 4.2 of the book
# "Modern Tkinter for Busy Python Programmers

# Adaptado na oficina Python Prático com Luciano Ramalho no
# no Garoa Hacker Club.

import tkinter as tk
from tkinter import N, W, E, S, ttk

def calculate(*args):
  try:
    value = float(feet.get())
    meters.set(value * 0.3048)
  except ValueError:
    pass

root = tk.Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack()
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)

feet = tk.StringVar()
meters = tk.StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
  child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()