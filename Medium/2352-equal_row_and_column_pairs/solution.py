from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Count the number of pairs where a row and a column are identical.

        A pair (r, c) is considered equal if the r-th row and c-th column
        contain the same elements in the same order.

        :param grid: A square matrix of integers
        :return: The number of equal row-column pairs
        """
        n = len(grid)
        result = 0

        # Convert rows to tuples for hashing
        rows = [tuple(row) for row in grid]

        # Build column tuples
        columns = []
        for col in range(n):
            column = []
            for row in range(n):
                column.append(grid[row][col])
            columns.append(tuple(column))

        # Count occurrences of rows and columns
        row_count = Counter(rows)
        col_count = Counter(columns)

        # Count matching row-column pairs
        for row, freq in row_count.items():
            if row in col_count:
                result += freq * col_count[row]

        return result
