from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Check whether a matrix is a Toeplitz matrix.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # 1. Classic Toeplitz matrix (square)
        (
            [
                [1, 2, 3],
                [4, 1, 2],
                [5, 4, 1]
            ],
            True
        ),

        # 2. Rectangular Toeplitz matrix
        (
            [
                [3, 7, 0, 9],
                [5, 3, 7, 0],
                [6, 5, 3, 7]
            ],
            True
        ),

        # 3. Not a Toeplitz matrix (diagonal mismatch)
        (
            [
                [1, 2, 3],
                [4, 9, 2],
                [5, 4, 1]
            ],
            False
        ),

        # 4. Single row (always Toeplitz)
        (
            [
                [1, 2, 3, 4]
            ],
            True
        ),

        # 5. Single column (always Toeplitz)
        (
            [
                [1],
                [2],
                [3]
            ],
            True
        ),

        # 6. Minimal matrix (1×1)
        (
            [
                [42]
            ],
            True
        ),
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = solution.isToeplitzMatrix(matrix)
        print(f"Test Case {i}: {'PASS' if result == expected else 'FAIL'}")
        print(f"Matrix: {matrix}")
        print(f"Expected: {expected}, Got: {result}\n")
