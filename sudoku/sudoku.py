import random as r
import tkinter as tk
from tkinter import Button, Entry, Label, LabelFrame, Text

root = tk.Tk() # Create root window
root.title("Sudoku") # Window Title
root.geometry("400x200") # Window Size
# root.resizable(0, 0)

def randomInt():
    random_number = r.randint(1, 9)
    return random_number

# Game Grid
game_frame = LabelFrame(root, )
game_frame.grid(row=0, column=0)

top_left_grid = LabelFrame(game_frame, )
top_center_grid = LabelFrame(game_frame, )
top_right_grid = LabelFrame(game_frame, )
middle_left_grid = LabelFrame(game_frame, )
middle_center_grid = LabelFrame(game_frame, )
middle_right_grid = LabelFrame(game_frame, )
bottom_left_grid = LabelFrame(game_frame, )
bottom_center_grid = LabelFrame(game_frame, )
bottom_right_grid = LabelFrame(game_frame, )

top_left_grid.grid(row=0, column=0)
top_center_grid.grid(row=0, column=1)
top_right_grid.grid(row=0, column=2)
middle_left_grid.grid(row=1, column=0)
middle_center_grid.grid(row=1, column=1)
middle_right_grid.grid(row=1, column=2)
bottom_left_grid.grid(row=2, column=0)
bottom_center_grid.grid(row=2, column=1)
bottom_right_grid .grid(row=2, column=2)

# Buttons Frame
btns_frame = LabelFrame(root, )
btns_frame.grid(row=0, column=1) # Position for all buttons
# Buttons (controls padding)
btn1 = Button(btns_frame, text="1", padx=20 ,pady=15)
btn2 = Button(btns_frame, text="2", padx=20 ,pady=15)
btn3 = Button(btns_frame, text="3", padx=20 ,pady=15)
btn4 = Button(btns_frame, text="4", padx=20 ,pady=15)
btn5 = Button(btns_frame, text="5", padx=20 ,pady=15)
btn6 = Button(btns_frame, text="6", padx=20 ,pady=15)
btn7 = Button(btns_frame, text="7", padx=20 ,pady=15)
btn8 = Button(btns_frame, text="8", padx=20 ,pady=15)
btn9 = Button(btns_frame, text="9", padx=20 ,pady=15)
# Button Grid (controls margins)
btn1.grid(row=0, column=1, padx=2 ,pady=2)
btn2.grid(row=0, column=2, padx=2 ,pady=2)
btn3.grid(row=0, column=3, padx=2 ,pady=2)
btn4.grid(row=1, column=1, padx=2 ,pady=2)
btn5.grid(row=1, column=2, padx=2 ,pady=2)
btn6.grid(row=1, column=3, padx=2 ,pady=2)
btn7.grid(row=2, column=1, padx=2 ,pady=2)
btn8.grid(row=2, column=2, padx=2 ,pady=2)
btn9.grid(row=2, column=3, padx=2 ,pady=2)

root.mainloop()