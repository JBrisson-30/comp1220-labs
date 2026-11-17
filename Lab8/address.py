"""Part C. Where a table entry sits in memory (Section 8.3).

A table with `cols` columns is stored one row after another (row major order),
starting at memory address `x`. Rows and columns are counted from 1.
Replace `pass` with one line.
"""


def address(x, cols, row, col):
    """Return the address of the entry at the given row and column."""

    starting_point = x

    # get to Row starting with row
    # we need to add row X cols

    return starting_point + (row - 1) * cols + (col - 1)
