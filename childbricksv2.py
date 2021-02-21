from brickv2 import Brick
from grid import  Board
from constants import max_col,max_row
from colorama import *
init()


class Brick1(Brick):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.colour=Back.LIGHTYELLOW_EX
        self.power="1"

    

class Brick2(Brick):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.colour=Back.RED
        self.power="2"
    #polymorphism
    def degrade(self,grid):
        if(self.power=="2"):
            self.colour=Back.LIGHTYELLOW_EX
            self.power="1"
            self.create_brick(grid,self.colour,self.power)
        elif(self.power=="1"):
            self.gone=1
            for j in range(self.ylen):
                grid[self.x][self.y+j]=" "


        

class Brick3(Brick):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.colour=Back.BLUE
        self.power="!"
    def degrade(self,grid):
        for j in range(self.ylen):
                grid[self.x][self.y+j]=self.colour+self.power+ Style.RESET_ALL
        

        
    


        
    





# testing:

# b1=Board(max_row,max_col)
# b1.create_board()

# paddle=Paddle()
# b1.grid=paddle.intialrender(b1.grid)

# brick1=Brick1(0,51)
# brick1.create_brick(b1.grid,brick1.colour,brick1.power)

# brick3=Brick1(0,75)
# brick3.create_brick(b1.grid,brick3.colour,brick3.power)

# brick5=Brick1(0,99)
# brick5.create_brick(b1.grid,brick5.colour,brick5.power)

# brick6=Brick1(0,123)
# brick6.create_brick(b1.grid,brick6.colour,brick6.power)

# __________________________________________________________
# brick2=Brick2(0,63)
# b1.grid=brick2.create_brick(b1.grid,brick2.colour)

# brick4=Brick2(0,87)
# b1.grid=brick4.create_brick(b1.grid,brick4.colour)

# brick6=Brick2(0,111)
# b1.grid=brick6.create_brick(b1.grid,brick6.colour)

# brick8=Brick3(0,135)
# b1.grid=brick8.create_brick(b1.grid,brick8.colour)


# b1.print_board()  
