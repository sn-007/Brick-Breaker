from brick import Brick,os
from grid import max_col,max_row, Board
from colorama import *
init()


class Brick1(Brick):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.colour=Back.LIGHTYELLOW_EX

class Brick2(Brick):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.colour=Back.RED
        

class Brick3(Brick):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.colour=Back.CYAN
        self.ylen=9
    
    def create_brick(self,grid,colour):
        for i in range(self.xlen):
            for j in range(self.ylen):
                grid[self.x+i][self.y+j]=colour+" " + Style.RESET_ALL
        for j in range(self.ylen):
            grid[self.x+self.xlen-1][self.y+j]=colour+"_" + Style.RESET_ALL


        return grid




# #testing:
# os.system('clear')
# b1=Board(max_row,max_col)
# b1.create_board()

# # paddle=Paddle()
# # b1.grid=paddle.intialrender(b1.grid)

# brick1=Brick1(0,51)
# b1.grid=brick1.create_brick(b1.grid,brick1.colour)

# brick3=Brick1(0,75)
# b1.grid=brick3.create_brick(b1.grid,brick3.colour)

# brick5=Brick1(0,99)
# b1.grid=brick5.create_brick(b1.grid,brick5.colour)

# brick6=Brick1(0,123)
# b1.grid=brick6.create_brick(b1.grid,brick6.colour)

# #__________________________________________________________
# brick2=Brick2(0,63)
# b1.grid=brick2.create_brick(b1.grid,brick2.colour)

# brick4=Brick2(0,87)
# b1.grid=brick4.create_brick(b1.grid,brick4.colour)

# brick6=Brick2(0,111)
# b1.grid=brick6.create_brick(b1.grid,brick6.colour)

# brick8=Brick3(0,135)
# b1.grid=brick8.create_brick(b1.grid,brick8.colour)





# b1.print_board()  
