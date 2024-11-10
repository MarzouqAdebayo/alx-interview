#!/usr/bin/env python3
"""Module for testing '0-nqueens.py' """
import unittest

m = __import__("0-nqueens")


class TestNQueens(unittest.TestCase):
    def test_valid_diagonals(self):
        N = 4
        y = 2
        x = 1
        want = [(0, 1), (1, 2), (2, 3), (0, 3), (2, 1), (3, 0)]
        got = m.get_all_diagonals(N, x, y)
        self.assertEqual(len(want), len(got))
        for item in got:
            self.assertTrue(True if item in want else False)
        N = 6
        want = [(0, 1), (1, 2), (2, 3), (0, 3), (2, 1), (3, 0), (3, 4), (4, 5)]
        got = m.get_all_diagonals(N, x, y)
        print(want)
        print(got)
        self.assertEqual(len(want), len(got))
        for item in got:
            self.assertTrue(True if item in want else False)

    def test_valid_square(self):
        N = 4
        possible_solution = [[0, 0], [3, 3]]
        y = 2
        x = 1
        got = m.is_valid_square(N, possible_solution, x, y)
        self.assertTrue(got)

    def test_invalid_square(self):
        N = 4
        y = 2
        x = 1
        possible_solution = [[0, 0], [1, 3], [3, 2]]
        got = m.is_valid_square(N, possible_solution, x, y)
        self.assertFalse(got)
