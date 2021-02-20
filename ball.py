from colorama import *
from constants import *


class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.xspeed=-1
        self.yspeed=1
        self.lives=3

    def move(self,paddle,grid):
        px=paddle.xrow
        py=paddle.ycol
        if(self.y+self.yspeed >= right_wall or self.y+self.yspeed <= left_wall ):
            self.yspeed*=-1
            
        if(self.x+self.xspeed <= top_wall ):
            self.xspeed*=-1
        
        
#checking collison ball vs paddle XD
        if(self.x+self.xspeed > paddle_xrow-1):

            if(py <= self.y <= py+paddle_length-1 ):
                self.xspeed*=-1
            else:
                grid[self.x][self.y]=" "
                self.x=ball_startx
                self.y=ball_starty
                self.xspeed=-1
                self.yspeed=1
                paddle.xrow=paddle_xrow
                paddle.ycol=paddle_ycol
                paddle.intialrender(grid)
                self.lives-=1
                return 0
            
        self.y=self.y+self.yspeed
        self.x=self.x+self.xspeed
        return 1

    

    
    def update_ball(self,grid):
        grid[self.x][self.y]= Fore.BLUE+"0"+Style.RESET_ALL
        prevx=self.x-self.xspeed
        prevy=self.y-self.yspeed
        if(prevx <= paddle_xrow-1):
            grid[prevx][prevy]= " "
        return grid
    
    def launch(self,grid,paddle):
        ball_cond=self.move(paddle,grid)
        
        grid=self.update_ball(grid)

        return grid,ball_cond





