from grid import *
from colorama import *
import time
init()

class Paddle:

    def __init__(self):
        self.length=10
        self.xrow=28
        self.ycol=90

    def render_paddle(self, grid):
        for i in range(self.length):
            grid[self.xrow][self.ycol+i] = Back.BLACK+" "+Style.RESET_ALL
        grid[self.xrow][self.ycol+self.length-1]=" "
        grid[self.xrow][self.ycol+self.length-2]=" "
    
        return grid
    
    def move_paddle_left(self):
        if(self.ycol > 50):
            self.ycol-=2
    
    def move_paddle_right(self):
        self.ycol+=2
        




#intiialising grid
b1=Board(max_row,max_col)
b1.create_board()

#creating paddle
paddle= Paddle()


for i in range(10):
    if(True):
        #moving paddle
        paddle.move_paddle_left()

        #updating grid with paddle
        b1.grid= paddle.render_paddle(b1.grid)

        #prinitng background
        b1.print_board()
    # else:
    #     paddle.move_paddle_right()
    #     b1.grid= paddle.render_paddle(b1.grid)
    #     b1.print_board()
    time.sleep(0.13)
        








