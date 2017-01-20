import numpy as np
def legal_move(move, current_1, current_2, maze):
    if move.lower() == "up":
        if maze[current_1-1, current_2] != '#':
            new_position = current_1-1, current_2
            return True, new_position
    if move.lower() == "down":
        if maze[current_1 + 1, current_2] != '#':
            new_position = current_1 + 1, current_2
            return True, new_position
    if move.lower() == "right":
        if maze[current_1, current_2 + 1] != '#':
            new_position = current_1, current_2 + 1
            return True, new_position
    if move.lower() == "left":
        if maze[current_1, current_2 - 1] != '#':
            new_position = current_1, current_2 - 1
            return True, new_position
# def maze_step(move, current_1, current_2, new_maze, end_1, end_2, turn):
#     legal, new_position = legal_move(move, current_1, current_2, new_maze)
#     if legal == True:
#         print new_position[0]
#         print new_position[1]
#         new_maze[new_position[0], new_position[1]] = '.'
#         current_pos_1 = new_position[0]
#         current_pos_2 = new_position[1]
#         print new_maze
#
#         if new_maze[end_1, end_2] != '.':
#             maze_game(new_maze, turn + 1, current_pos_1, current_pos_2)
#         else:
#             print "You win!"
#
#         return legal

def maze_game(maze, turn =1, current_1 =0, current_2 = 0):

    if turn == 1:
        start_1 = str(np.where(maze=='S'))[8]
        start_2 = str(np.where(maze=='S'))[20]
        current_1 = int(start_1)
        current_2 = int(start_2)

    end_1 = str(np.where(maze == 'E'))[8]
    end_2 = str(np.where(maze == 'E'))[20]

    print maze

    new_maze = maze.copy()
    game_finish = False

    while game_finish == False:

        move = raw_input("Where would you like to move (up, down, left, or right)?")
        # legal, new_position = legal_move(move, current_1, current_2, new_maze)

        legal, new_position = legal_move(move, current_1, current_2, maze)
        if legal != True:
            print "That is an impossible move, please select a new move"
            continue
        print new_position[0]
        print new_position[1]
        new_maze[new_position[0], new_position[1]] = '.'
        current_pos_1 = new_position[0]
        current_pos_2 = new_position[1]
        print new_maze

        if new_maze[end_1, end_2] != '.':
            maze_game(new_maze, turn + 1, current_pos_1, current_pos_2)
        else:
            print "Maze completed!"

        break
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
