import numpy as np
import random

def legal_move(move, row, column, maze, max_row_column):
    possibilities = ["up", "down", "right", "left"]
    reset_row = row
    reset_column = column
    if move == possibilities[0]:
        row -= 1
    if move == possibilities[1]:
        row += 1
    if move == possibilities[2]:
        column += 1
    if move == possibilities[3]:
        column -= 1
    print "legal row", row
    print "legal column", column
    if row > max_row_column or column > max_row_column or row < 0  or column < 0 or maze[row, column] != 'o' or maze[row, column] == '.':
        return False, reset_row, reset_column
    if maze[row, column] == 'o':
        return True, row, column


def neighbor(maze, row, column, maxdim, open_neighbors):

    # if maze[row+1, column] == 'o' or maze[row-1, column] == 'o' or maze[row, column+1] == 'o' or maze[row, column-1] == 'o':
    if row+1 < maxdim and maze[row+1, column] == 'o':
        open_neighbors.append((row+1, column))
    if row-1 >=0 and maze[row-1, column] == 'o':
        open_neighbors.append((row-1, column))
    if column+1<maxdim and maze[row, column + 1] == 'o':
        open_neighbors.append((row, column+1))
    if column-1 >=0 and maze[row, column - 1] == 'o':
        open_neighbors.append((row, column-1))


        print "True"
        return True, open_neighbors
    else:
        print "False"
        return False, None


def generate_a_maze(dimension, maze_grid = False, start_row = None, start_column = None, end_row = None, end_column = None):
    if maze_grid == False:
        maze = np.chararray((dimension, dimension))
        maze[:] = 'o'
        maze_grid = maze.copy()
        maze_grid[0, random.randint(0, dimension - 1)] = 'E'
        maze_grid[dimension - 1, random.randint(0, dimension - 1)] = 'S'
        start_row, start_column = np.where(maze_grid == 'S')
        start_row, start_column = (int(start_row[0]), int(start_column[0]))
        end_row, end_column = np.where(maze_grid == 'E')
        end_row, end_column = (int(end_row[0]), int(end_column[0]))
        backtracking_list = []

        maze_grid1 = maze_grid.copy()
        maze_grid2 = maze_grid.copy()
        maze_grid3 = maze_grid.copy()
        maze_grid4 = maze_grid.copy()

    print maze_grid



    # define backtracking list and available neighbors list
    backtracking_list.append((start_row, start_column))
    open_neighbors = []

    while backtracking_list:
        print backtracking_list
        # loops through until backtracking list is empty, essentially when we have reached the initial position
        if maze_grid[end_row, end_column] == 0:
            return True, maze_grid
        neighbor_is_available, open_neighbors = neighbor(maze_grid, start_row, start_column, dimension - 1, open_neighbors)
        maze_grid[start_row, start_column] = '.'
        if neighbor_is_available:
            print "open neighbors", open_neighbors
            new_position = open_neighbors[random.randint(0, len(open_neighbors) - 1)]
            maze_grid[new_position] = '.'
            print maze_grid
            backtracking_list.append(new_position)
            print backtracking_list
            print
        else:
            start_row, start_column = backtracking_list.pop()
            # continue

    # for move in ["up", "down", "right", "left"]:
    #     legal, new_row, new_column = legal_move(move, start_row, start_column, maze_grid, dimension-1)
    #     print "open neighbors", open_neighbors
    #     if legal:
    #         # allowed_moves.append((new_row, new_column))
    #
    #         while backtracking_list:
    #             maze_grid[start_row, start_column] = '.'
    #             neighbor_is_available, open_neighbors = neighbor(maze_grid, new_row, new_column,
    #                                                                         dimension - 1, open_neighbors)
    #             if neighbor_is_available:
    #                 print open_neighbors
    #                 new_position = open_neighbors[random.randint(0, len(open_neighbors)-1)]
    #             else:
    #                 new_row, new_column = backtracking_list.pop()

            # while 'o' in maze_grid:
            #     neighbor_is_available, random_row, random_column = neighbor(maze_grid, new_row, new_column, dimension-1)
            #     if neighbor_is_available:
            #         allowed_moves.append((new_row, new_column))
            #         maze_grid[new_row, new_column] = '.'
            #         print maze_grid
            #         new_row = random_row
            #         new_column = random_column
            #         maze_grid[new_row, new_column] = '.'
            #     if not neighbor_is_available and allowed_moves != []:
            #         new_row, new_column = allowed_moves.pop()






generate_a_maze(5)