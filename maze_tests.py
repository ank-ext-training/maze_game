import unittest
import numpy as np
from legal_move import legal_move
from maze_step import maze_step

maze_grid = np.array([['#', '#', 'E', '#', '#'],
                          [' ', ' ', ' ', '#', '#'],
                          ['#', ' ', '#', '#', '#'],
                          [' ', ' ', '#', ' ', '#'],
                          ['#', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', '#'],
                     [' ', ' ', '#', ' ', '#'],
                     ['#', '#', ' ', ' ', '#'],
                     ['#', ' ', ' ', '#', '#'],
                     ['#', ' ', ' ', ' ', 'S']])

maze_grid2 = np.array([['#', '#', 'E', '#', '#'],
                          [' ', ' ', ' ', '#', '#'],
                          ['#', ' ', '#', '#', '#'],
                          [' ', ' ', '#', ' ', '#'],
                          ['#', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', '#'],
                     [' ', ' ', '#', ' ', '#'],
                     ['#', '#', ' ', ' ', '#'],
                     ['#', ' ', ' ', '#', '#'],
                     ['#', ' ', '.', '.', 'S']])

class TestMaze(unittest.TestCase):
    def test_move_rejection(self):
        expected_result1 = False
        expected_result2 = 0
        print expected_result1, expected_result2
        move1 = "up"
        current1 = 9
        current2 = 4
        maze = maze_grid
        actual_result1, actual_result2 = legal_move(move1, current1, current2, maze)
        print actual_result1, actual_result2
        self.assertTrue(actual_result1 == expected_result1)
        self.assertTrue(actual_result2 == expected_result2)

    def test_move_acceptance(self):
        expected_result1 = True
        expected_result2 = 9,3
        print expected_result1, expected_result2
        move1 = "left"
        current1 = 9
        current2 = 4
        maze = maze_grid
        actual_result1, actual_result2 = legal_move(move1, current1, current2, maze)
        print actual_result1, actual_result2
        self.assertTrue(actual_result1 == expected_result1)
        self.assertTrue(actual_result2 == expected_result2)

    def test_visited(self):
        # in the human interaction case, allow user to move to already visited places so he/she can backtrack
        expected_result1 = True
        expected_result2 = 9, 3
        print expected_result1, expected_result2
        move1 = "right"
        current1 = 9
        current2 = 2
        maze = maze_grid
        actual_result1, actual_result2 = legal_move(move1, current1, current2, maze)
        print actual_result1, actual_result2
        self.assertTrue(actual_result1 == expected_result1)
        self.assertTrue(actual_result2 == expected_result2)





