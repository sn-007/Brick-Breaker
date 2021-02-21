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
        
        
        
           

    
        


        
    
        



