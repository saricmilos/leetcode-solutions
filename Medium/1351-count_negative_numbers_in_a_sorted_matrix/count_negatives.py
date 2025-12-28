from typing import List

class Solution:
    """
    Solution for LeetCode 1351: Count Negative Numbers in a Sorted Matrix.

    Given a m x n matrix `grid` which is sorted in non-increasing order 
    both row-wise and column-wise, this class provides a method to count 
    all negative numbers in the matrix efficiently.
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Counts the number of negative numbers in a sorted matrix.

        Args:
            grid (List[List[int]]): 2D list of integers sorted in non-increasing 
                                    order row-wise and column-wise.

        Returns:
            int: The total count of negative numbers in the matrix.
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        row, col = 0, n - 1  # Start from the top-right corner

        while row < m and col >= 0:
            if grid[row][col] < 0:
                # All elements below in this column are negative
                count += m - row
                col -= 1  # Move left
            else:
                row += 1  # Move down if current element is non-negative

        return count
