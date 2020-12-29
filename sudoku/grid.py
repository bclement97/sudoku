import numpy as np


class Grid:
    DIM = 9
    BOX_DIM = 3
    SIZE = (DIM, DIM)
    EMPTY_CELL = 0

    def __init__(self, src: np.ndarray = None):
        self._M = src.reshape(Grid.SIZE) if src is not None else np.zeros(Grid.SIZE)

    def col(self, i: int) -> np.ndarray:
        return self._M[:, i]

    def row(self, i: int) -> np.ndarray:
        return self._M[i, :]

    def box(self, i: int) -> np.ndarray:
        # Since NumPy is row major, so are the boxes
        col_start = i // self.BOX_DIM
        col_end = col_start + self.BOX_DIM
        row_start = i % self.BOX_DIM
        row_end = row_start + self.BOX_DIM
        return self._M[col_start:col_end, row_start:row_end]

    def get(self, col: int, row: int) -> int:
        return self._M[col, row]

    def set(self, col: int, row: int, value: int) -> bool:
        self._M[col, row] = value
        return self.validate_cell(col, row)

    def clear(self, col: int, row: int) -> None:
        self.set(col, row, Grid.EMPTY_CELL)

    def validate_cell(self, col: int, row: int) -> bool:
        def validate_group(cells: np.ndarray) -> bool:
            elems = cells[cells != Grid.EMPTY_CELL]
            return elems.size == np.unique(elems).size

        box = self.BOX_DIM * (row // self.BOX_DIM) + col // self.BOX_DIM
        valid_col = validate_group(self.col(col))
        valid_row = validate_group(self.row(row))
        valid_box = validate_group(self.box(box))
        return valid_col and valid_row and valid_box
