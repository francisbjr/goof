import pygame
from sudokuGame.sudoku import Sudoku
from sudokuGame.constants import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def main():
    run = True
    clock = pygame.time.Clock() 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
        pygame.display.update()

    pygame.quit()

# Driver code
if __name__ == "__main__":
    N = 9
    K = 30 # Number of fill in spaces
    sudoku = Sudoku(N, K)
    sudoku.fillValues()
    sudoku.printSudoku()

    main()