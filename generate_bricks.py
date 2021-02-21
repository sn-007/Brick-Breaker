from brickv2 import Brick
from constants import *
from childbricksv2 import Brick1, Brick2, Brick3
import random
from time_score import update_score

allbricks=[]

def generate_bricks(grid):
    
    for i in range (2,max_row-white_board_len,4):

        y1=random.randint(left_wall, right_wall-brick_length-3)
        
        b=random.randint(1,9)

        if(7 <= b <=9):
            brick=Brick1(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            allbricks.append(brick)

        elif ( 3 <= b <=6):
            brick=Brick2(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            allbricks.append(brick)
        
        elif (1<= b <=2):
            brick=Brick3(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            allbricks.append(brick)


def check_collison(grid,ball):
    x=ball.x
    y=ball.y
    
    for block in allbricks:
        if(block.gone==1):
            for j in range (block.ylen):
                grid[block.x][block.y+j]=" "
            continue
        if(block.power=="1" or block.power=='2'):
            if( (block.x==x-1 or block.x==x+1 ) and (block.y <= y <= block.y + block.ylen-1 ) ):
                block.degrade(grid)
                ball.score+=1
                update_score(grid,ball.score)
                grid[x][y]=" "
                if(ball.xspeed < 0):
                    ball.xspeed*=-1
                    ball.x=ball.x+ball.xspeed
                elif(ball.xspeed > 0):
                    ball.x=ball.x-ball.xspeed
                    ball.xspeed*=-1
        else:
            if( (block.x==x-1 or block.x==x+1 ) and (block.y <= y <= block.y + block.ylen-1 ) ):

                grid[x][y]=" "
                if(ball.xspeed < 0):
                    ball.xspeed*=-1
                    ball.x=ball.x+ball.xspeed
                elif(ball.xspeed > 0):
                    ball.x=ball.x-ball.xspeed
                    ball.xspeed*=-1



    
            



            


