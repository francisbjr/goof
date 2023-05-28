import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk() # Creates window / root

canvas = tk.Canvas(root, height=600, width=600, bg="gray") 
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8)

root.mainloop()

########### fucntions ##############