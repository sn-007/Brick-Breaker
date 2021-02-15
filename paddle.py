from grid import *
from colorama import *
import time
init()

class Paddle:

    def __init__(self):
        self.length=10
        self.xrow=28
        self.ycol=90
        self.movingflag="0"
        

    def intialrender(self,grid):
        for i in range(self.length):
            grid[self.xrow][self.ycol+i] = Back.BLACK+" "+Style.RESET_ALL
        return grid

    def move_paddle_left(self,grid):
        if(self.ycol > 52):
            self.ycol-=2
            for j in range(max_col):
                grid[self.xrow][j]=" "
            for i in range(self.length):
                grid[self.xrow][self.ycol+i] = Back.BLACK+" "+Style.RESET_ALL
            # if(self.movingflag=="L"):
            #     grid[self.xrow][self.ycol+self.length-1]=" "
            #     grid[self.xrow][self.ycol+self.length-2]=" "
            # self.movingflag="L"
    
        return grid
    
    def move_paddle_right(self,grid):
        if(self.ycol + 9 < 141):
            self.ycol+=2
            for j in range(max_col):
                grid[self.xrow][j]=" "
            for i in range(self.length):
                grid[self.xrow][self.ycol+i] = Back.BLACK+" "+Style.RESET_ALL
            # if(self.movingflag=="R")
            #     grid[self.xrow][self.ycol]=" "
            #     grid[self.xrow][self.ycol+1]=" "
               
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
        








