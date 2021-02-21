def printtime(loopstart,starttime,grid):
    current_time=int(loopstart-starttime)
    for i in range(3):
        grid[3][7-i]=current_time%10
        current_time= int(current_time/10)
def allocate_grid_for_time(grid):
    grid[3][0]="T"
    grid[3][1]="I"
    grid[3][2]="M"
    grid[3][3]="E"
    grid[3][4]=":"
    grid[3][5]=0
    grid[3][6]=0
    grid[3][7]=0
    grid[3][8]="s"
    grid[3][9]="e"
    grid[3][10]="c"

def allocate_grid_for_score(grid):
    grid[5][0]="S"
    grid[5][1]="C"
    grid[5][2]="O"
    grid[5][3]="R"
    grid[5][4]="E"
    grid[5][5]=":"
    grid[5][6]=0
    grid[5][7]=0
def allocate_grid_for_lives(grid):
    grid[7][0]="L"
    grid[7][1]="I"
    grid[7][2]="V"
    grid[7][3]="E"
    grid[7][4]="S"
    grid[7][5]=":"
    grid[7][6]=3

def printlives(lives,grid):
    grid[7][6]=lives

def update_score(grid,score):
    grid[5][7]=score%10
    if(score > 10):
        score/=10
        score=int(score)
    else:
        score=0
    grid[5][6]=score
