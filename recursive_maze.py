import numpy as np
from supporting import legal_move, maze_initialization


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

# same thing holds here. If you are re-using same snipped of code in serverala locations, it's usually
# better to encapsulate it as a function and import when you need it.

def recursive_maze_wrapper(maze):
    current_row, current_column, end_1, end_2, number_rows, number_columns = maze_initialization(maze)
    solved, solution = recursive_maze(maze, current_row, current_column, end_1, end_2,
                                        number_rows, number_columns)

    if not solved:
        print 'Maze is unsolvable'
        return None

    else:
        print 'Maze solved!'
        return solution


def recursive_maze(maze, current_row, current_column, end1, end2, number_of_rows, number_of_columns):
    new_maze = maze.copy()
    # There is a slight problem here: you are mixing out-of scope with in-the scope elements

    # I think it's more a question whether an exist cannot be be reached. It's more a question of
    # knowing if everything has been explored - no more legal moves left. Hence the check was moved
    # to the function wrapper

    if new_maze[end1, end2] == '.':
        print "Maze Completed!"
        print new_maze
        return True, new_maze

    # you don't really need it - we know it will be true because the line above will exit otherwise

    possible_moves = []
    for move in ["up", "down", "right", "left"]:
        legal, new_row, new_column = legal_move(move, current_row, current_column,
                                                        new_maze, number_of_rows, number_of_columns)
        if legal:
            possible_moves.append((new_row, new_column))

    if possible_moves:
        for new_row, new_column in possible_moves:  # we could eventually make the if/else here implicit
            new_maze[new_row, new_column] = '.'
            solved, solution = recursive_maze(new_maze, new_row, new_column, end1, end2,
                                              number_of_rows, number_of_columns)
            # if we found a solution, we will need to propagate the solution upwards, as well
            if solved:
                print "propagating solution upwards!"
                return True, solution

    else:
        print "this branch is a dead-end"  #and maze is unsolvable when all braches are dead-ends
        return False, None


if __name__ == '__main__':
    print recursive_maze_wrapper(maze)
