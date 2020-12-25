import numpy as np


class Puzzle:
    def __init__(self):
        self._M = np.zeros(9, 9)

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
        return self.validate_entry(col, row)

    def clear(self, col: int, row: int) -> None:
        self.set(col, row, 0)

    def validate_entry(self, col: int, row: int) -> bool:
        def validate(entries: np.ndarray) -> bool:
            nonzero_entries = entries[entries > 0]
            return nonzero_entries.size == np.unique(nonzero_entries).size

        box = 3*(row//3) + col//3
        valid_col = validate(self.col(col))
        valid_row = validate(self.row(row))
        valid_box = validate(self.box(box))
        return valid_col and valid_row and valid_box
