from paddle import Paddle, max_col,max_row
from input import Get, input_to
from grid import Board,os
from childbricksv2 import Brick1,Brick2,Brick3
import time
from ball import Ball
from time_score import printlives, printtime, allocate_grid_for_time, allocate_grid_for_score, allocate_grid_for_lives
from constants import *
from generate_bricks import generate_bricks, check_collison
from colorama import *
init()

#starttime
starttime=time.time()
os.system('clear')

#declaring board along with grid
b1=Board(max_row,max_col)
b1.create_board()




#time scores and lives handling
current_time=0
allocate_grid_for_time(b1.grid)
allocate_grid_for_score(b1.grid)
allocate_grid_for_lives(b1.grid)




#paddle oblect declaration 
paddle=Paddle()
paddle.intialrender(b1.grid)

#ball object declaration
ball=Ball(ball_startx,ball_starty)
b1.grid=ball.update_ball(b1.grid)
ball_flag=0

b1.print_board()

#bricks Generation:
generate_bricks(b1.grid,ball)

powerup=False
while(True):
    check_collison(b1.grid,ball)
    loopstart=time.time()
    current_time=int(loopstart-starttime)
    printtime(loopstart,starttime,b1.grid)
    printlives(ball.lives,b1.grid)

    

    
    getch=Get()
    key=input_to(getch)
    if(ball_flag==1):
        b1.grid,ball_flag=ball.launch(b1.grid,paddle)


    if(key == 'a'):
        b1.grid=paddle.move_paddle_left(b1.grid)
        if(ball_flag==0 and left_wall + 3 <= ball.y <=right_wall ):
            b1.grid[ball.x][ball.y]=" "
            ball.y=ball.y-paddle_speed
            b1.grid[ball.x][ball.y]=Fore.BLUE+"0"+Style.RESET_ALL
        

    elif(key == 'd'):
        b1.grid=paddle.move_paddle_right(b1.grid)
        if(ball_flag==0 and left_wall <= ball.y <=right_wall-3):
            b1.grid[ball.x][ball.y]=" "
            ball.y=ball.y+paddle_speed
            b1.grid[ball.x][ball.y]=Fore.BLUE+"0"+Style.RESET_ALL
        
    elif(key == 'l' and ball_flag==0):
        b1.grid,ball_cond=ball.launch(b1.grid,paddle)
        ball_flag=1


    elif(key=="."):
        break

    if(ball.lives==0 or ball.rem==0):
        printlives(ball.lives,b1.grid)
        b1.print_board()
        break
    
    b1.print_board()
    loopend=time.time()
    looptime=loopend-loopstart
    if(looptime < 0.1):
        time.sleep(0.1-looptime)
    

print("Ended BRO Your SCORE SEE TOP LEFT")
    
    
    
        
    



