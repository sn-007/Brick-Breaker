from constants import *
from colorama import *
import time
init()

class Paddle:

    def __init__(self):
        self.length=paddle_length
        self.xrow=paddle_xrow
        self.ycol=paddle_ycol
        

    def intialrender(self,grid):

        for i in range(self.ycol):
            grid[self.xrow][i]=" "


        for i in range(self.length):
            grid[paddle_xrow][paddle_ycol+i] = Back.BLACK+" "+Style.RESET_ALL
        

    def move_paddle_left(self,grid):
        if(self.ycol > left_wall+1):
            self.ycol-=paddle_speed
            for j in range(max_col):
                grid[self.xrow][j]=" "
            for i in range(self.length):
                grid[self.xrow][self.ycol+i] = Back.BLACK+" "+Style.RESET_ALL
            
    
        return grid
    
    def move_paddle_right(self,grid):
        if(self.ycol + paddle_length < right_wall-1):
            self.ycol+=paddle_speed
            for j in range(max_col):
                grid[self.xrow][j]=" "
            for i in range(self.length):
                grid[self.xrow][self.ycol+i] = Back.BLACK+" "+Style.RESET_ALL
            
               
        return grid
    
        





        








