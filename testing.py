from paddle import Paddle, max_col,max_row
from input import Get, input_to
from grid import Board,os
from childbricks import Brick1,Brick2,Brick3
import time
from ball import Ball


os.system('clear')
b1=Board(max_row,max_col)
b1.create_board()

paddle=Paddle()
b1.grid=paddle.intialrender(b1.grid)

ball=Ball(27,95)
b1.grid=ball.update_ball(b1.grid)
ball_flag=0

b1.print_board()


while(True):
    getch=Get()
    key=input_to(getch)
    # if(key=="None"):
    #     continue
    #print(key)
    if(ball_flag==1):
        b1.grid=ball.launch(b1.grid)


    if(key == 'a'):
        b1.grid=paddle.move_paddle_left(b1.grid)
        

    elif(key == 'd'):
        b1.grid=paddle.move_paddle_right(b1.grid)
        
    elif(key == 'l' and ball_flag==0):
        b1.grid=ball.launch(b1.grid)
        ball_flag=1

    elif(key=="."):
        break
    b1.print_board()


    
    
    
        
    



