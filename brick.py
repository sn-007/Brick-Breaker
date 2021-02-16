from grid import max_col,max_row, Board
from colorama import *
import time
import os
from paddle import Paddle
init()

class Brick:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.xlen=3
        self.ylen=12

    def create_brick(self,grid,colour):
        for i in range(self.xlen):
            for j in range(self.ylen):
                 grid[self.x+i][self.y+j]=colour+" " + Style.RESET_ALL
        #grid[self.x][self.y]=Back.LIGHTRED_EX+" " + Style.RESET_ALL
        return grid
            
        
#testing

# os.system('clear')
# b1=Board(max_row,max_col)
# b1.create_board()

# paddle=Paddle()
# b1.grid=paddle.intialrender(b1.grid)

# brick=Brick(0,51)
# b1.grid=brick.create_brick(b1.grid)
# b1.grid[0][63]=Back.RED+" " + Style.RESET_ALL

# b1.print_board()
           

    
        


        
    
        



