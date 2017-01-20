import numpy as np
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

start_row = str(np.where(maze == 'S'))[8]
start_column = str(np.where(maze == 'S'))[20]
current_row = int(start_row)
current_column = int(start_column)
end_1 = str(np.where(maze == 'E'))[8]
end_2 = str(np.where(maze == 'E'))[20]
number_rows = maze.shape[0]-1
number_columns = maze.shape[1]-1

def recursive_maze(maze, current_row, current_column, end1, end2, number_of_rows, number_of_columns):
    new_maze = maze.copy()
    if new_maze[end1, end2] == '.':
        print "Maze Completed!"
        return new_maze
    if new_maze[end_1, end_2] != '.':
        possibilities = ["up", "down", "right", "left"]
        for move in possibilities:
            reset_row = current_row
            reset_column = current_column
            if move.lower() == possibilities[0]:
                current_row = current_row - 1
            elif move.lower() == possibilities[1]:
                current_row = current_row + 1
            elif move.lower() == possibilities[2]:
                current_column = current_column + 1
            else:
                current_column = current_column - 1
            if current_row > number_rows or current_column > number_columns or current_row < 0 or current_column < 0:
                current_row = reset_row
                current_column = reset_column
                continue

            if new_maze[current_row, current_column] == '#' or new_maze[current_row, current_column] == '.' or new_maze[current_row, current_column] == 'S':
                current_row = reset_row
                current_column = reset_column
                continue

            if new_maze[current_row, current_column] != '#' and new_maze[current_row, current_column] != '.':
                new_maze[current_row, current_column] = '.'
                recursive_maze(new_maze, current_row, current_column, end_1, end_2, number_rows,number_columns)
            recursive_maze(new_maze, reset_row, reset_column, end_1, end_2,number_rows, number_columns)

    else:
        print "This is an unsolvable maze!"

recursive_maze(maze, current_row, current_column
