import random
import math
import tkinter as tk
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

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

        button = ttk.Button(self, text="Easy",
                            command=lambda: controller.show_frame(EasyModePage))
        button.pack()

        button2 = ttk.Button(self, text="Hard",
                            command=lambda: controller.show_frame(HardModePage))
        button2.pack()

class EasyModePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Easy Mode", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = ttk.Button(self, text="Hard",
                            command=lambda: controller.show_frame(HardModePage))
        button2.pack()

class HardModePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Hard Mode", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = ttk.Button(self, text="Easy",
                            command=lambda: controller.show_frame(EasyModePage))
        button2.pack()
        
class Sudoku:
    def __init__(self, N, K):
        self.N = N
        self.K = K
 
        # Compute square root of N
        SRNd = math.sqrt(N)
        self.SRN = int(SRNd)
        self.mat = [[0 for _ in range(N)] for _ in range(N)]
     
    def fillValues(self):
        # Fill the diagonal of SRN x SRN matrices
        self.fillDiagonal()
 
        # Fill remaining blocks
        self.fillRemaining(0, self.SRN)
 
        # Remove Randomly K digits to make game
        self.removeKDigits()
     
    def fillDiagonal(self):
        for i in range(0, self.N, self.SRN):
            self.fillBox(i, i)
     
    def unUsedInBox(self, rowStart, colStart, num):
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[rowStart + i][colStart + j] == num:
                    return False
        return True
     
    def fillBox(self, row, col):
        num = 0
        for i in range(self.SRN):
            for j in range(self.SRN):
                while True:
                    num = self.randomGenerator(self.N)
                    if self.unUsedInBox(row, col, num):
                        break
                self.mat[row + i][col + j] = num
     
    def randomGenerator(self, num):
        return math.floor(random.random() * num + 1)
     
    def checkIfSafe(self, i, j, num):
        return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i - i % self.SRN, j - j % self.SRN, num))
     
    def unUsedInRow(self, i, num):
        for j in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
     
    def unUsedInCol(self, j, num):
        for i in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
    
    def fillRemaining(self, i, j):
        # Check if we have reached the end of the matrix
        if i == self.N - 1 and j == self.N:
            return True
     
        # Move to the next row if we have reached the end of the current row
        if j == self.N:
            i += 1
            j = 0
     
        # Skip cells that are already filled
        if self.mat[i][j] != 0:
            return self.fillRemaining(i, j + 1)
     
        # Try filling the current cell with a valid value
        for num in range(1, self.N + 1):
            if self.checkIfSafe(i, j, num):
                self.mat[i][j] = num
                if self.fillRemaining(i, j + 1):
                    return True
                self.mat[i][j] = 0
         
        # No valid value was found, so backtrack
        return False
 
    def removeKDigits(self):
        count = self.K
 
        while (count != 0):
            i = self.randomGenerator(self.N) - 1
            j = self.randomGenerator(self.N) - 1
            if (self.mat[i][j] != 0):
                count -= 1
                self.mat[i][j] = 0
        return
 
    def printSudoku(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.mat[i][j], end=" ")
            print()

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