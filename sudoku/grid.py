import numpy as np


class Grid:
    DIM = 9
    SIZE = (DIM, DIM)

    def __init__(self, src: np.ndarray = None):
        self._M = src.reshape(Grid.SIZE) if src is not None else np.zeros(Grid.SIZE)

    def col(self, i: int) -> np.ndarray:
        return self._M[:, i]

    def row(self, i: int) -> np.ndarray:
        return self._M[i, :]

    def box(self, i: int) -> np.ndarray:
        # Since NumPy is row major, so are the boxes
        col_start = i // 3
        row_start = i % 3
        return self._M[col_start:col_start+3, row_start:row_start+3]

    def get(self, col: int, row: int) -> int:
        return self._M[col, row]

    def set(self, col: int, row: int, value: int) -> bool:
        self._M[col, row] = value
        return self.validate_cell(col, row)

    def clear(self, col: int, row: int) -> None:
        self.set(col, row, 0)

    def validate_cell(self, col: int, row: int) -> bool:
        def validate_group(elems: np.ndarray) -> bool:
            nonzero_elems = elems[elems > 0]
            return nonzero_elems.size == np.unique(nonzero_elems).size

        box = 3*(row//3) + col//3
        valid_col = validate_group(self.col(col))
        valid_row = validate_group(self.row(row))
        valid_box = validate_group(self.box(box))
        return valid_col and valid_row and valid_box
