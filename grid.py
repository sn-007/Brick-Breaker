from colorama import *
import os
from constants import *



init()
class Board:

    #Creates the entire board for the game

    #constructor function
    def __init__(self, rows,cols):
        self.__rows=rows
        self.__cols=cols
        self.grid=[]
       

    #function to create the playing board
    def create_board(self):
        for i in range(self.__rows):
            self.temp=[]
            for j in range(self.__cols):
                if(j == left_wall or j == right_wall):
                    self.temp.append("|")
                else:
                    self.temp.append(" ")
            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)



    
        

    #function to print the playing board
    def print_board(self):
        #os.system('clear')
        print("\033[%d;%dH" % (0, 0))
     
        for i in range(0, self.__rows-white_board_len):
            for j in range (self.__cols):
                if(j > left_wall and j < right_wall):
                    print(Back.LIGHTGREEN_EX +self.grid[i][j] + Back.RESET, end='')

                else:
                    print(self.grid[i][j],end='')
            print()
        for i in range(self.__rows-white_board_len, self.__rows):
            for j in range (self.__cols):
                
                if(j > left_wall and j < right_wall):
                    print(Back.WHITE +self.grid[i][j] + Back.RESET, end='')

                else:
                    print(self.grid[i][j],end='')
            print()
        
        
        
