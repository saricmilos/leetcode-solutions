"""
LeetCode 867 - Transpose Matrix

Problem:
Given a 2D integer matrix, return its transpose. The transpose of a
matrix switches the rows and columns.

Technique Used:
- Nested loops for row/column swapping
- List comprehension for matrix initialization

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Transposes the input 2D matrix.

        :param matrix: List[List[int]] - original matrix
        :return: List[List[int]] - transposed matrix
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize transposed matrix with switched dimensions
        transpose_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

        # Fill the transposed matrix
        for i in range(rows):
            for j in range(cols):
                transpose_matrix[j][i] = matrix[i][j]

        return transpose_matrix


if __name__ == "__main__":
    # Runnable examples
    solution = Solution()

    test_matrices = [
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2], [3, 4], [5, 6]],
        [[1]],
    ]

    for matrix in test_matrices:
        print("Original Matrix:")
        for row in matrix:
            print(row)
        print("Transposed Matrix:")
        for row in solution.transpose(matrix):
            print(row)
        print()