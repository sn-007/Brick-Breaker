from brickv2 import Brick
from constants import *
from childbricksv2 import Brick1, Brick2, Brick3
import random
from time_score import update_score
from colorama import *

init()

allbricks=[]
stop=0
def generate_bricks(grid,ball):

    ball.rem=0
    
    for i in range (2,max_row-white_board_len,4):

        y1=random.randint(left_wall+3, right_wall-brick_length-3)
        
        b=random.randint(1,3)

        if(i%3==1):
            brick=Brick1(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            ball.rem+=1
            allbricks.append(brick)



        elif (i%3==2):
            brick=Brick2(i,y1)
            brick.create_brick(grid,brick.colour,brick.power)
            ball.rem+=2
            allbricks.append(brick)
        
        else:
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
                ball.rem-=1
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



    
            



            


