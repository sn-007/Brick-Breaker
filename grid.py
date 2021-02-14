from colorama import *
import os
init()
max_row=30
max_col=190
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
                if(j == 50 or j == 144):
                    self.temp.append("|")
                else:
                    self.temp.append(" ")
            self.grid.append(self.temp)
        # self.grid=np.array(self.grid)



    
        

    #function to print the playing board
    def print_board(self):
        os.system('clear')
     
        for i in range(0, self.__rows-5):
            for j in range (self.__cols):
                if(j > 50 and j < 144):
                    print(Back.LIGHTGREEN_EX +self.grid[i][j] + Back.RESET, end='')

                else:
                    print(self.grid[i][j],end='')
            print()
        for i in range(self.__rows-5, self.__rows):
            for j in range (self.__cols):
                
                if(j > 50 and j < 144):
                    print(Back.WHITE +self.grid[i][j] + Back.RESET, end='')

                else:
                    print(self.grid[i][j],end='')
            print()
        
        
        
