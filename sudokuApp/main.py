import tkinter as tk
from tkinter import ttk
from sudokuGame.sudoku import Sudoku
from sudokuGame.constants import LARGE_FONT

##### Classes #####
class windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Sudoku")
        tk.Tk.geometry(self, "400x400")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, EasyModePage, HardModePage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        canvas = tk.Canvas(self, cursor="cross")   
        board = canvas.create_rectangle(20,20, 1, 1, outline='red')
        canvas.pack()

        button = ttk.Button(self, text="Easy", command=lambda: controller.show_frame(EasyModePage))
        button.pack()

        button2 = ttk.Button(self, text="Hard", command=lambda: controller.show_frame(HardModePage))
        button2.pack()

class EasyModePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Easy Mode", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = ttk.Button(self, text="Hard", command=lambda: controller.show_frame(HardModePage))
        button2.pack()

class HardModePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Hard Mode", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = ttk.Button(self, text="Easy", command=lambda: controller.show_frame(EasyModePage))
        button2.pack()

##### Functions #####
def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()
'''
game_frame = LabelFrame(root, )
game_frame.grid(row=0, column=0) # Position of game board 

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
'''
# Driver code
if __name__ == "__main__":
    N = 9
    K = 30 # Number of fill in spaces
    sudoku = Sudoku(N, K)
    sudoku.fillValues()
    sudoku.printSudoku()

    root = windows()
    root.mainloop()