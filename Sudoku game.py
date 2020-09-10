# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:10:27 2020

@author: Sven
"""

from tkinter import *
import tkinter.ttk as ttk
import numpy as np
import random as rand
from time import sleep

root = Tk()
root.title("Sudoku")
root.geometry('510x600')

#Topmenu
menu_frame = Frame(root)
menu_frame.pack()
#top_text = Label(menu_frame, text="Sudoku")
#top_text.pack(side= LEFT)

#Sudoku Frame
sudoku_frame = Frame(root)
sudoku_frame.pack()
sudoku_frame_size=500
sudoku = Canvas(sudoku_frame, bd = 0, bg = "white",height=sudoku_frame_size, width = sudoku_frame_size)
sudoku.pack()

#Sudoku Body
sudoku_size = sudoku_frame_size-5
box_size = sudoku_size/9
x_offset = 4
y_offset = 4

#Number row Frame
number_row_frame = Frame(root)
number_row_frame.pack()
number_row = Canvas(number_row_frame, bd=0, bg="white",height=box_size+3,width=sudoku_frame_size)
number_row.pack()

#display thicc gridlines
def showgrid():
    global x_offset, y_offset, sudoku_size
    for i in range(1,3):
        sudoku.create_line(x_offset, i*sudoku_size/3 + y_offset, sudoku_size + x_offset, i*sudoku_size/3 + y_offset, width=5)
        sudoku.create_line(i*sudoku_size/3 + x_offset, 0 + y_offset, i*sudoku_size/3 + x_offset, sudoku_size + y_offset, width=5) 

#Creates a news class called Tile.
class Tile:
    selected = False
    def __init__(self, x, y, ID, number):
        self.x = x
        self.y = y
        self.ID = ID
        self.number = number
        self.tile_length = sudoku_size/9
        self.frame = sudoku
    
    #returns the center of the tile in xy-coordinates
    def center(self):
        return [self.x + 0.5 * self.tile_length, self.y + 0.5 * self.tile_length]
    
    #displays the tile with a black border if it's not selected and with a red border if it is selected (clicked)
    def display(self):
        if self.number == 0:
            self.number = ""
        feature = ["white",1]
        if self.selected is True:
            feature = ["yellow",2]
        self.frame.create_rectangle(self.x, self.y, self.x + self.tile_length, self.y + self.tile_length,fill=feature[0], outline="black", width=feature[1], tag=self.ID)
        self.frame.create_text(self.center()[0], self.center()[1],text=str(self.number), tag=self.ID, font=("Arial",28))
        self.frame.tag_bind(self.ID,'<ButtonPress-1>',self.click)
        showgrid()
    
    #displays indexlines around the selected tile
    def index(self, x_tile, y_tile):
        color = "red"
        global x_indexlines, y_indexlines, index_box, x_offset, y_offset, box_size, sudoku_size
        for i in range(2):       
            sudoku.delete(x_indexlines[i])
            sudoku.delete(y_indexlines[i])
            x_indexlines[i] = sudoku.create_line(x_tile * box_size + i * box_size + x_offset , y_offset, 
                                                 x_tile * box_size + i * box_size + x_offset , sudoku_size + y_offset,
                                                 width=2, fill = color)
            y_indexlines[i] = sudoku.create_line(x_offset, y_tile * box_size + i * box_size + y_offset, 
                                                 sudoku_size + x_offset , y_tile * box_size + i * box_size + y_offset,
                                                 width=2, fill = color)
            sudoku.delete(index_box[i])
            index_box[i] = sudoku.create_rectangle(x_tile*box_size + x_offset, y_tile*box_size + y_offset,
                                                   x_tile*box_size + box_size + x_offset, y_tile*box_size + box_size + y_offset,
                                                   outline="red",width=2)
            showgrid()      
    
    #if the tile is clicked, its selection status gets updated, and the indexlines and red border will be displayed        
    def click(self, event):
        global current_tile
        deselect()
        self.selected = True
        self.display()
        self.index(tile(event.x),tile(event.y))
        current_tile = self.ID
        print("Click!!! \n x: {x}, y: {y} \n tile ID: {t1},{t2}".format(x = event.x, y=event.y, t1=tile(event.x), t2=tile(event.y)))
        
    #changes the value of the tile if it is a possible value
    def SetNumber(self,value):
        if possible(current_sudoku,tile(self.y),tile(self.x),int(value)) is True:
            self.number = value
            #current_sudoku[tile(self.y),tile(self.x)] = value
            self.display()
            self.index(tile(self.x),tile(self.y))

#class for tiles that can change the tile values in the sudoku
class SelectionTile(Tile):
    def __init__(self, x, y, ID, number):
        super().__init__(x,y,ID,number)
        self.frame = number_row
    def __repr__(self):
        return "{} {} {} {}".format(self.x,self.y,self.ID,self.number)
    def display(self):
        super().display()
        self.frame.tag_bind(self.ID,'<ButtonPress-1>',self.click)
    def index(self):
        pass
    def click(self, event):
        #print("click")
        tiles[current_tile].SetNumber(self.ID[-1])
        

#no idea why this has to be done, but it works..
class indexline:
    pass
x_indexlines = [indexline for i in range(2)]
y_indexlines = [indexline for i in range(2)]
index_box = [indexline for i in range(2)]     
#################################################

#converts x,y coordinates to tile ID
def tile(coord):
    return int((coord-x_offset)/box_size)

#function that deselects all tiles
def deselect():
    for tile in tiles:
        tiles[tile].selected = False
        tiles[tile].display()

def generate_sudoku(entry):
    global tiles
    tiles = {}
    for i in range(9):
        for j in range(9):
            x = i * box_size + x_offset
            y = j * box_size + y_offset
            tiles["{x},{y}".format(x=i,y=j)] = Tile(x,y,"{x},{y}".format(x=i,y=j),entry[j,i])
            tiles["{x},{y}".format(x=i,y=j)].display()
    return tiles

#display selection tiles
selection_tiles = {}
for i in range(1,10):
    selection_tiles["{}".format(i)] = SelectionTile((i-1) * box_size + x_offset, y_offset,"ST"+str(i),i)
    selection_tiles["{}".format(i)].display()

#Check if value n can be inserted at x,y#
def possible(array,y,x,n): 
    for i in range(0,9):
        if array[i,x] == n:
            return False
        if array[y,i] == n:
            return False
    x0 = (x//3) *3
    y0 = (y//3) *3
    for i in range(0,3):
        for j in range(0,3):
            if array[y0+j,x0+i] == n:
                return False
    return True

#check if sudoku is finished
def check(array):
    for i in range(9):
        for j in range(9):
            if array[i,j]==0:
                return False
    return True

#solve sudoku
counter =0
def solve(board):
    global counter
    if check(board):
        return True
    else:
        for y in range(9):
            for x in range(9):
                if board[y,x] == 0:
                    for k in range(1,10):
                        if possible(board,y,x,k):
                            board[y,x]=k
                            if check(board):
                                counter += 1
                            if solve(board):
                                return True
                            board[y,x]=0
                    return False

#solve button##################### 
def button_solve():
    #solve(current_sudoku)
    generate_sudoku(solved_sudoku)
                
button_solve = Button(menu_frame, text="solve",font=("Arial",10),command=button_solve)
button_solve.pack(side= RIGHT)  

#Generate new sudoku puzzel
sudoku_row = np.array([1,2,3,4,5,6,7,8,9])
def generate_new_full_grid(new_sudoku):
    global sudoku_row
    if check(new_sudoku):
        return True
    else:
        for row in range(9):
            for col in range(9):
                if new_sudoku[row,col] == 0:
                    rand.shuffle(sudoku_row)
                    for value in sudoku_row:
                        if possible(new_sudoku,row,col,value):
                            new_sudoku[row,col]=value
                            if generate_new_full_grid(new_sudoku):
                                return True
                            new_sudoku[row,col]=0
                    return False

def generate_new_sudoku(new_sudoku,difficulty):
    global counter, solved_sudoku
    gaps = np.count_nonzero(new_sudoku == 0)
    while gaps <= difficulty:
        row = rand.randrange(0,9)
        col = rand.randrange(0,9)
        while new_sudoku[row,col] == 0:
            row = rand.randrange(0,9)
            col = rand.randrange(0,9)
        backup = np.copy(new_sudoku)
        counter = 0
        new_sudoku[row,col] = 0
        gaps = np.count_nonzero(new_sudoku == 0)
        solve(np.copy(new_sudoku))        
        if counter != 1:
            new_sudoku = backup
            counter = 0
    solved_sudoku = np.copy(new_sudoku)
    solve(solved_sudoku)
    return new_sudoku

current_sudoku = None
solved_sudoku = None
def create_new():
    global current_sudoku, difficulty_input
    new_sudoku = np.zeros((9,9))
    generate_new_full_grid(new_sudoku)
    new_sudoku = new_sudoku.astype(int)
    generate_new_sudoku(new_sudoku,difficulty[difficulty_input.get()])
    print(difficulty[difficulty_input.get()])
    current_sudoku = new_sudoku
    generate_sudoku(current_sudoku)
    print(current_sudoku)


text_difficulty = Label(menu_frame, text='Difficulty: ')
text_difficulty.pack(side = LEFT)
difficulty = {'Easy':40, 'Medium':46, 'Hard':54}
difficulty_input = StringVar(menu_frame)   
optionmenu_difficulty = ttk.OptionMenu(menu_frame, difficulty_input, 'Easy', 'Easy', 'Medium', 'Hard')  
optionmenu_difficulty.pack(side = LEFT)
text_spacing = Label(menu_frame, text='     ')
text_spacing.pack(side = LEFT) 
print(difficulty[difficulty_input.get()])

                
button_create_new = Button(menu_frame, text="Create new",font=("Arial",10),command=create_new)
button_create_new.pack(anchor =W)  


#Selected tile
current_tile = None

#Generating the sudoku
create_new()
tiles = generate_sudoku(current_sudoku)


showgrid()
root.mainloop()








