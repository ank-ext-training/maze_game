import numpy as np
def legal_move(move, current_1, current_2, maze):
    possibilities = ["up", "down", "right", "left", '#']
    if move.lower() == possibilities[0]:
        current_1 = current_1-1
    if move.lower() == possibilities[1]:
        current_1 = current_1 + 1
    if move.lower() == possibilities[2]:
        current_2 = current_2 + 1
    if move.lower() == possibilities[3]:
        current_2 = current_2 - 1
    if maze[current_1, current_2] != '#':
        new_position = current_1, current_2
        return True, new_position
    else:
        return False, 0

def maze_step(move, current_1, current_2, new_maze, end_1, end_2):
    legal, new_position = legal_move(move, current_1, current_2, new_maze)
    if legal == True:
        new_maze[new_position[0], new_position[1]] = '.'
        current_1 = new_position[0]
        current_2 = new_position[1]
        return legal, new_maze, current_1, current_2

    else:
        return False, new_maze, current_1, current_2

def maze_game(maze, current_1 =0, current_2 = 0):
    start_1 = str(np.where(maze=='S'))[8]
    start_2 = str(np.where(maze=='S'))[20]
    current_1 = int(start_1)
    current_2 = int(start_2)
    end_1 = str(np.where(maze == 'E'))[8]
    end_2 = str(np.where(maze == 'E'))[20]
    new_maze = maze.copy()

    while new_maze[end_1, end_2] != '.':
        print "Current Game State:"
        print new_maze
        move = raw_input("Where would you like to move (up, down, left, or right)? \n")
        legal, new_maze, current_1, current_2 = maze_step(move, current_1, current_2, new_maze, end_1, end_2)
        if not legal:
            print "\n That is an impossible move, please select a new move"
            continue
    print "Maze Completed!"
    return new_maze

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

maze_game(maze)
