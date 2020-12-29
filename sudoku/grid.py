import numpy as np


class Grid:
    DIM = 9
    BOX_DIM = 3
    SIZE = (DIM, DIM)
    EMPTY_CELL = 0

    def __init__(self, src: np.ndarray = None):
        self._M = (src.reshape(Grid.SIZE) if src is not None
                   else np.full(Grid.SIZE, Grid.EMPTY_CELL))

    def row(self, i: int) -> np.ndarray:
        """Return the i-th row."""
        return self._M[i, :]

    def col(self, i: int) -> np.ndarray:
        """Return the i-th column."""
        return self._M[:, i]

    def box(self, i: int) -> np.ndarray:
        """Return the i-th row-major box."""
        row_start = Grid.BOX_DIM * (i // Grid.BOX_DIM)
        row_end = row_start + Grid.BOX_DIM
        col_start = Grid.BOX_DIM * (i % Grid.BOX_DIM)
        col_end = col_start + Grid.BOX_DIM
        return self._M[row_start:row_end, col_start:col_end]

    def get(self, row: int, col: int) -> int:
        """Get the element of a cell."""
        return self._M[row, col]

    def set(self, row: int, col: int, elem: int) -> bool:
        """Set a cell and return if the element is valid."""
        self._M[row, col] = elem
        return self.validate_cell(row, col)

    def clear(self, row: int, col: int) -> None:
        """Clear a cell."""
        self._M[row, col] = Grid.EMPTY_CELL

    def validate_cell(self, row: int, col: int) -> bool:
        """Ensure the row, column, and box of a cell are valid."""

        def validate_group(cells: np.ndarray) -> bool:
            """Ensure a group of cells has no duplicate elements."""
            elems = cells[cells != Grid.EMPTY_CELL]
            return elems.size == np.unique(elems).size

        box = Grid.BOX_DIM * (row // Grid.BOX_DIM) + col // Grid.BOX_DIM
        valid_row = validate_group(self.row(row))
        valid_col = validate_group(self.col(col))
        valid_box = validate_group(self.box(box))
        return valid_row and valid_col and valid_box
