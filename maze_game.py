import numpy as np
from supporting import maze_initialization

# it's not a great idea to duplicate methods you can have elsewhere
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

    if current_1 > number_rows or current_2 > number_columns or current_1 < 0 or current_2 < 0 or \
                    maze[current_1, current_2] == '#':
        # backtrack prevention is only needed in case of recursive solving - in the main game it should be there
        # however, if we can backtrack in the normal game, we could have our position marked with an
        # x. can you implement that one?
        return False, reset_row, reset_column

    if maze[current_1, current_2] != '#':
        return True, current_1, current_2


def maze_step(move, current_1, current_2, new_maze, number_rows, number_columns):
    print current_1, current_2
    legal, current_1, current_2 = legal_move(move, current_1, current_2, new_maze, number_rows, number_columns)
    if legal:
        new_maze[current_1, current_2] = '.'
        return legal, new_maze, current_1, current_2

    else:
        return False, new_maze, current_1, current_2


def maze_game(maze):
    current_1, current_2, end_1, end_2, number_rows, number_columns = maze_initialization(maze)
    new_maze = maze.copy()

    while new_maze[end_1, end_2] != '.':
        print "Current Game State:"
        print new_maze
        move = raw_input("Where would you like to move (up, down, left, or right)? \n")
        legal, new_maze, current_1, current_2 = maze_step(move, current_1, current_2, new_maze, number_rows, number_columns)
        if not legal:
            print "\n That is an impossible move, please select a new move"
            continue
    print "Maze Completed!"
    return new_maze


maze_1 = np.array([['#', '#', 'E', '#', '#'],
                   [' ', ' ', ' ', '#', '#'],
                   ['#', ' ', '#', '#', '#'],
                   [' ', ' ', '#', ' ', '#'],
                   ['#', ' ', ' ', ' ', '#'],
                   ['#', ' ', '#', ' ', '#'],
                   [' ', ' ', '#', ' ', '#'],
                   ['#', '#', ' ', ' ', '#'],
                   ['#', ' ', ' ', '#', '#'],
                   ['#', ' ', ' ', ' ', 'S']])


maze_game(maze_1)
