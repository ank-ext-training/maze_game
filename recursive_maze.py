import numpy as np
import legal_move
maze = np.array([['#', '#', 'E', '#', '#'],
                          [' ', ' ', ' ', '#', '#'],
                          ['#', ' ', '#', '#', '#'],
                          [' ', ' ', '#', ' ', '#'],
                          ['#', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', '#'],
                     [' ', ' ', '#', ' ', '#'],
                     ['#', '#', ' ', ' ', '#'],
                     ['#', ' ', ' ', '#', '#'],
                     ['#', ' ', ' ', ' ', 'S']])
current_row = int(str(np.where(maze == 'S'))[8])
current_column = int(str(np.where(maze == 'S'))[20])
if 'E' in maze:
    end_1 = str(np.where(maze == 'E'))[8]
    end_2 = str(np.where(maze == 'E'))[20]
else:
    end_1 = None
    end_2 = None
number_rows = maze.shape[0]-1
number_columns = maze.shape[1]-1

def recursive_maze(maze, current_row, current_column, end1, end2, number_of_rows, number_of_columns):
    new_maze = maze.copy()
    if end1 == None or end_2 == None:
        print "This maze has no exit!"
        return new_maze
    if new_maze[end1, end2] == '.':
        print "Maze Completed!"
        print new_maze
        return new_maze
    elif new_maze[end_1, end_2] != '.':
        possibilities = ["up", "down", "right", "left"]
        for move in possibilities:
            reset_row = current_row
            reset_column = current_column
            legal, current_row, current_column = legal_move.legal_move(move, current_row, current_column, new_maze, number_rows, number_columns)
            if legal == False:
                current_row = reset_row
                current_column = reset_column
                continue

            else:
                new_maze[current_row, current_column] = '.'
                recursive_maze(new_maze, current_row, current_column, end_1, end_2, number_rows,number_columns)
            recursive_maze(new_maze, reset_row, reset_column, end_1, end_2,number_rows, number_columns)

    else:
        print "This is an unsolvable maze!"

recursive_maze(maze, current_row, current_column, end_1, end_2, number_rows, number_columns)
