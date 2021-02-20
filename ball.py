from colorama import *


class Ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.xspeed=-1
        self.yspeed=1

    def move(self):
        if(self.y+self.yspeed >= 144 or self.y+self.yspeed <= 50 ):
            self.yspeed*=-1
            
        if(self.x+self.xspeed >= 28 or self.x+self.xspeed <= 0 ):
            self.xspeed*=-1
            
        self.y=self.y+self.yspeed
        self.x=self.x+self.xspeed

    

    
    def update_ball(self,grid):
        grid[self.x][self.y]= Fore.BLUE+"0"+Style.RESET_ALL
        prevx=self.x-self.xspeed
        prevy=self.y-self.yspeed
        if(prevx <= 27):
            grid[prevx][prevy]= " "
        

        return grid
    
    def launch(self,grid):
        self.move()
        grid=self.update_ball(grid)
        return grid





