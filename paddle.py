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
        for i in range(self.length):
            grid[self.xrow][self.ycol+i] = Back.BLACK+" "+Style.RESET_ALL
        return grid

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
    
        





# #testing bro


# #intiialising grid
# b1=Board(max_row,max_col)
# b1.create_board()

# #creating paddle
# paddle= Paddle()
# #b1.grid=paddle.intialrender(b1.grid)


# for i in range(100):

#     if(i%3==1):
#         b1.grid =paddle.move_paddle_left(b1.grid)
#         b1.print_board()

#     elif(i%3==2):
#         b1.grid =paddle.move_paddle_right(b1.grid)
#         b1.print_board()
       
#     time.sleep(0.1)
        








