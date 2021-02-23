import numpy as np
import pytest

from sudoku.grid import Grid


@pytest.fixture
def solution_grid_fake():
    return Grid(np.arange(Grid.DIM**2))


@pytest.fixture
def partial_grid_1():
    return Grid(np.array([[0, 7, 4, 2, 0, 0, 0, 0, 0],
                          [9, 0, 0, 6, 0, 0, 1, 0, 2],
                          [0, 0, 1, 8, 3, 0, 0, 6, 9],
                          [0, 9, 2, 4, 0, 0, 0, 0, 7],
                          [0, 4, 0, 1, 0, 5, 0, 8, 0],
                          [3, 0, 0, 0, 0, 2, 5, 9, 0],
                          [1, 3, 0, 0, 7, 6, 4, 0, 0],
                          [8, 0, 5, 0, 0, 1, 0, 0, 6],
                          [0, 0, 0, 0, 0, 8, 3, 5, 0]]))


@pytest.fixture
def solution_grid_1():
    return Grid(np.array([[6, 7, 4, 2, 1, 9, 8, 3, 5],
                          [9, 8, 3, 6, 5, 7, 1, 4, 2],
                          [2, 5, 1, 8, 3, 4, 7, 6, 9],
                          [5, 9, 2, 4, 8, 3, 6, 1, 7],
                          [7, 4, 6, 1, 9, 5, 2, 8, 3],
                          [3, 1, 8, 7, 6, 2, 5, 9, 4],
                          [1, 3, 9, 5, 7, 6, 4, 2, 8],
                          [8, 2, 5, 3, 4, 1, 9, 7, 6],
                          [4, 6, 7, 9, 2, 8, 3, 5, 1]]))