from constants import max_col,max_row,brick_length
from colorama import *
import time
import os
from paddle import Paddle
from grid import Board
init()

class Brick:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ylen=brick_length
        self.gone=0

        

    def create_brick(self,grid,colour,power):
        for j in range(self.ylen):
                grid[self.x][self.y+j]=colour+power+ Style.RESET_ALL
    
    def degrade(self,grid):
        self.gone=1
        for j in range(self.ylen):
                grid[self.x][self.y+j]=" "
        
        
            
        
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
           

    
        


        
    
        



