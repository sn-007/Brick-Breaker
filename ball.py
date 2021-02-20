from colorama import *
from constants import *


class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.xspeed=-1
        self.yspeed=1

    def move(self):
        if(self.y+self.yspeed >= right_wall or self.y+self.yspeed <= left_wall ):
            self.yspeed*=-1
            
        if(self.x+self.xspeed >= paddle_xrow or self.x+self.xspeed <= top_wall ):
            self.xspeed*=-1
            
        self.y=self.y+self.yspeed
        self.x=self.x+self.xspeed

    

    
    def update_ball(self,grid):
        grid[self.x][self.y]= Fore.BLUE+"0"+Style.RESET_ALL
        prevx=self.x-self.xspeed
        prevy=self.y-self.yspeed
        if(prevx <= paddle_xrow-1):
            grid[prevx][prevy]= " "
        

        return grid
    
    def launch(self,grid):
        self.move()
        grid=self.update_ball(grid)
        return grid





