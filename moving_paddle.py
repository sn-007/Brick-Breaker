from paddle import Paddle, max_col,max_row
from input import Get, input_to
from grid import Board,os
from childbricks import Brick1,Brick2,Brick3
import time


os.system('clear')
b1=Board(max_row,max_col)
b1.create_board()

paddle=Paddle()
paddle.intialrender(b1.grid)
bricks=[]
lastx=0
for countx in range (1,9):
    lasty=51
    for county in range (1,9):
        if(county!=8 and county%2==1):
            county+=1
            if(countx%2==1):
                temp=Brick1(lastx,lasty)
            else:
                temp=Brick2(lastx,lasty)

            b1.grid=temp.create_brick(b1.grid,temp.colour)
            lasty+=temp.ylen
            bricks.append(temp)
        elif(county!=8 and county%2==0):
            county+=1
            if(countx%2==1):
                temp=Brick2(lastx,lasty)
            else:
                temp=Brick1(lastx,lasty)
            b1.grid=temp.create_brick(b1.grid,temp.colour)
            lasty+=temp.ylen
            bricks.append(temp)
        else:
            county+=1
            temp=Brick3(lastx,lasty)
            b1.grid=temp.create_brick(b1.grid,temp.colour)
            lasty+=temp.ylen
            bricks.append(temp)
    lastx+=3
    countx+=1
    

# temp=Brick2(3,51)
# b1.grid=temp.create_brick(b1.grid,temp.colour)

b1.print_board()
#print(lastx)

while(True):
    getch=Get()
    key=input_to(getch)
    if(key=="None"):
        continue
    
    if(key == 'a'):
        b1.grid=paddle.move_paddle_left(b1.grid)
        b1.print_board()
    
    elif(key == 'd'):
        b1.grid=paddle.move_paddle_right(b1.grid)
        b1.print_board()
    elif(key=="."):
        break


    
    
    
        
    



