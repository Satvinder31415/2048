"""
Clone of the 2048 game
"""

import random

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def shift(lis,ind):
    """
    Function that shifts values
    """
    for index in range(ind,len(lis)-1):
        lis[index],lis[index+1] = lis[index+1],lis[index]
    return lis

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    res = []
    for ele in line:
        res.append(ele)
    for num in res:
        if num == 0:
            res = shift(res,res.index(num))
    for inde in range(len(res)-1):
        if res[inde] == res[inde+1]:
            res[inde] = res[inde] + res[inde+1]
            res[inde+1] = 0
    for num in res:
        if num == 0:
            res = shift(res,res.index(num))
    
    return res


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    height = 0          # height of the grid
    width  = 0          # width of the grid
    grid   = []         # grid
    initial_tiles = {}  # initial tiles for each direction

    def random_tile(self):
        """
        Selects a random tile from grid
        """
        random_row = random.randrange(0,self.height,1)
        random_col = random.randrange(0,self.width ,1)
        return random_row,random_col
    

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        rand_int = random.randrange(0,10,1)
        if rand_int == 4:
            var = 4
        else:
            var = 2
        flag = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    flag = 1
        if flag == 1:
            dummy_r,dummy_c = self.random_tile()
            while self.grid[dummy_r][dummy_c] != 0:
                dummy_r,dummy_c = self.random_tile()
            self.grid[dummy_r][dummy_c] = var

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.width)] for row in range(self.height)]
        self.new_tile()
        self.new_tile()
    
    def __init__(self,grid_height,grid_width):
        self.height = grid_height
        self.width  = grid_width
        self.reset()
        up_initial    = []
        down_initial  = []
        left_initial  = []
        right_initial = []
        for dummy_var in range(grid_height):
            left_initial.append((dummy_var,0))
            right_initial.append((dummy_var,grid_width-1))
        for dummy_var in range(grid_width):
            up_initial.append((0,dummy_var))
            down_initial.append((grid_height-1,dummy_var))
        self.initial_tiles['UP'] = up_initial
        self.initial_tiles['DOWN'] = down_initial
        self.initial_tiles['RIGHT'] = right_initial
        self.initial_tiles['LEFT'] = left_initial

    def __str__(self):
        """
        Returns string representation of grid
        """
        str_grid = ""
        for row in range(self.height):
            for col in range(self.width):
                temp = self.grid[row][col]
                str_grid += str(temp)
                str_grid += "  "
            str_grid += '\n'
        return str_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def set_tile(self,row,col,value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self,row,col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

    def print_initial_tiles(self):
        """
        Prints the set of initial tiles
        """
        for key,val in self.initial_tiles.items():
            print(key,val)

    def move(self,direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_tile_list = []
        if direction == UP:
            initial_tile_list = self.initial_tiles['UP']
        elif direction == DOWN:
            initial_tile_list = self.initial_tiles['DOWN']
        elif direction == LEFT:
            initial_tile_list = self.initial_tiles['LEFT']
        else:
            initial_tile_list = self.initial_tiles['RIGHT']

        flag = 0
        coord_list = []
        val_list   = []

        for element in initial_tile_list:
            del coord_list[:]
            del val_list[:]
            coord_list.append(element)
            val_list.append(self.grid[element[0]][element[1]])
            temp_row   = element[0]
            temp_col   = element[1]
            while(temp_col>-1 and temp_row>-1 and temp_row<self.height and temp_col<self.width):
                temp_row += OFFSETS[direction][0]
                temp_col += OFFSETS[direction][1]
                if temp_col>-1 and temp_row>-1 and temp_row<self.height and temp_col<self.width:
                    coord_list.append((temp_row,temp_col))
                    val_list.append(self.grid[temp_row][temp_col])
            val_list = merge(val_list)
            for elem in coord_list:
                if self.grid[elem[0]][elem[1]] != val_list[coord_list.index(elem)]:
                    flag = 1
                self.grid[elem[0]][elem[1]] = val_list[coord_list.index(elem)]
        if flag == 1: 
            self.new_tile()

    def check_if_won(self):
        """
        Returns 1 if player has won
        """
        flag = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 2048:
                    flag = 1
        return flag

    def check_if_lost(self):
        """
        Returns 1 if player has lost
        """
        flag = 1
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    flag = 0
        for row in range(self.height-1):
            for col in range(self.width-1):
                if self.grid[row][col] == self.grid[row+1][col] or self.grid[row][col] == self.grid[row][col+1]:
                    flag = 0
        for col in range(self.width-1):
            if self.grid[self.height-1][col] == self.grid[self.height-1][col+1]:
                flag = 0
        for row in range(self.height-1):
            if self.grid[row][self.width-1] == self.grid[row+1][self.width-1]:
                flag = 0
        return flag
        






