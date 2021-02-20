from brickv2 import Brick
from constants import *
from childbricksv2 import Brick1, Brick2, Brick3
import random

allbricks=[]
def generate_bricks(grid):
    
    for i in range (1,max_row-white_board_len,2):

        y1=random.randint(left_wall, right_wall-brick_length-3)
        
        b=random.randint(1,9)

        if(6 < b <=9):
            brick=Brick1(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            allbricks.append(brick)

        elif ( 3 < b <=6):
            brick=Brick2(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            allbricks.append(brick)
        
        elif (1<= b <=3):
            brick=Brick3(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            allbricks.append(brick)


def check_collison(grid,ball):
    x=ball.x
    y=ball.y
    
    for block in allbricks:
        if(block.power=="1"):
            if( (block.x <= x <= block.x+1) and (block.y <= y <= block.y + block.ylen-1 ) ):
                block.degrade(grid)
                ball.xspeed=-1


        elif(block.power=="2"):
            if( (block.x-2 <= x <= block.x+2) and (block.y <= y <= block.y + block.ylen-1 ) ):
                if(block.power=="2"):
                    ball.xspeed*=-1
                block.degrade(grid)
                

        elif(block.power=="!"):
            if( (block.x-2 <= x <= block.x+2) and (block.y <= y <= block.y + block.ylen-1 ) ):
                ball.xspeed*=-1
            



            


