class Powerup:
    def __init__(self,x,y,text):
        self.x=x
        self.y=y
        self.xspeed=1
        self.text=text
        self.active=0

    def fall(self,grid):
        grid[self.x][self.y]=" "
        self.x=self.x+self.xspeed
        grid[self.x][self.y]=self.text



    