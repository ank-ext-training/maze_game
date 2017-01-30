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
    if row > max_row_column or column > max_row_column or row < 0  or column < 0 or maze[row, column] != '#' or maze[row, column] == '.':
        return False, reset_row, reset_column, reset_row, reset_column
    if maze[row, column] == '#':
        return True, row, column, reset_row, reset_column


def generate_a_maze(dimension, maze_grid = False, start_row = None, start_column = None, end_row = None, end_column = None):
    if maze_grid == False:
        maze = np.chararray((dimension, dimension))
        maze[:] = '#'
        maze_grid = maze.copy()
        maze_grid[0, random.randint(0, dimension - 1)] = 'E'
        maze_grid[dimension - 1, random.randint(0, dimension - 1)] = 'S'
        start_row, start_column = np.where(maze_grid == 'S')
        start_row, start_column = (int(start_row[0]), int(start_column[0]))
        end_row, end_column = np.where(maze_grid == 'E')
        end_row, end_column = (int(end_row[0]), int(end_column[0]))
    print maze_grid


    print "start", start_row, start_column
    print "end", end_row, end_column

    allowed_moves = []
    for move in ["up", "down", "right", "left"]:
        print "move", move
        legal, new_row, new_column, reset_row, reset_column = legal_move(move, start_row, start_column, maze_grid, dimension-1)
        print legal
        if legal:
            print "legal-yes"
            print "new", new_row, new_column
            allowed_moves.append((new_row, new_column))
            print allowed_moves
            print maze_grid
            maze_grid[new_row, new_column] = 0
            print maze_grid
            new_row = reset_row
            new_column = reset_column

        print
    if allowed_moves:
        random_position = allowed_moves[random.randint(0, len(allowed_moves)-1)]
        print "random", random_position
        new_row = random_position[0]
        new_column = random_position[1]
        print allowed_moves
        type(allowed_moves)
        allowed_moves.remove(random_position)
        print "removed", allowed_moves
        print "length", len(allowed_moves)
        if len(allowed_moves) > 0:
            for row, column in allowed_moves:
                maze_grid[row, column] = '#'
        print maze_grid
        solved, solution = generate_a_maze(dimension, maze_grid=maze_grid, start_row=new_row, start_column=new_column, end_row=end_row, end_column=end_column)
        if solved:
            return True, solution



    if maze_grid[end_row, end_column] == '0':
        return maze_grid







generate_a_maze(5)
