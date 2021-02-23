import numpy as np
import pytest

from sudoku.grid import Grid


class TestGrid:
    def test_row(self, solution_grid_fake: Grid):
        for i in range(Grid.DIM):
            low = Grid.DIM * i
            high = Grid.DIM * (i + 1) - 1

            row = solution_grid_fake.row(i)
            
            assert row.size == Grid.DIM
            assert low == row[0]
            assert high == row[Grid.DIM - 1]

    def test_col(self, solution_grid_fake: Grid):
        for i in range(Grid.DIM):
            col = solution_grid_fake.col(i)
            assert col.size == Grid.DIM
