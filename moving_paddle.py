from paddle import *
from input import *
from grid import *
os.system('clear')
b1=Board(max_row,max_col)
b1.create_board()

paddle=Paddle()
b1.grid=paddle.intialrender(b1.grid)

b1.print_board()

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

    
    
    
        
    



