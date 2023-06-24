import pygame
from sudokuGame.sudoku import Sudoku
from sudokuGame.constants import LARGE_FONT

# Driver code
if __name__ == "__main__":
    N = 9
    K = 30 # Number of fill in spaces
    sudoku = Sudoku(N, K)
    sudoku.fillValues()
    sudoku.printSudoku()

    # root = windows()
    # root.mainloop()