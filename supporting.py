import numpy as np


def legal_move(move, current_1, current_2, maze, number_rows, number_columns):
    possibilities = ["up", "down", "right", "left"]
    reset_row = current_1
    reset_column = current_2

    if move.lower() == possibilities[0]:
        current_1 -= 1
    if move.lower() == possibilities[1]:
        current_1 += 1
    if move.lower() == possibilities[2]:
        current_2 += 1
    if move.lower() == possibilities[3]:
        current_2 -= 1

    if current_1 > number_rows or current_2 > number_columns or current_1 < 0 or current_2 < 0 or maze[current_1, current_2] == '#' or maze[current_1, current_2] == '.' or maze[current_1, current_2] == 'S':
        return False, reset_row, reset_column

    if maze[current_1, current_2] != '#':
        return True, current_1, current_2


def maze_initialization(maze):
    current_1, current_2 = np.where(maze == 'S')
    current_1, current_2 = (int(current_1[0]), int(current_2[0]))

    end_1, end_2 = np.where(maze == 'E')
    end_1, end_2 = (int(end_1[0]), int(end_2[0]))

    number_rows = maze.shape[0] - 1
    number_columns = maze.shape[1] - 1

    return current_1, current_2, end_1, end_2, number_rows, number_columns

