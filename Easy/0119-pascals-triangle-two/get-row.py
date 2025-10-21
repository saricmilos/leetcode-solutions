from typing import List

class Solution:
    """
    Solution for LeetCode 118: Pascal's Triangle

    Generates the first `numRows` rows of Pascal's Triangle.
    Each row starts and ends with 1, and each interior element
    is the sum of the two elements directly above it.

    Time Complexity: O(n^2), where n = numRows
    Space Complexity: O(n^2), for storing the triangle
    """

    def getRow(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's Triangle up to numRows.

        Args:
            numRows (int): Number of rows to generate.

        Returns:
            List[List[int]]: Pascal's Triangle represented as a list of rows.
        """
        pascals_triangle = [[1]]

        for row in range(1, numRows+1):
            pascals_row = [1]
            for element_in_row in range(1, row):
                pascals_row.append(
                    pascals_triangle[row - 1][element_in_row - 1] +
                    pascals_triangle[row - 1][element_in_row]
                )
            pascals_row.append(1)
            pascals_triangle.append(pascals_row)

        return pascals_triangle[numRows]


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.getRow(5))
    # Output:
    # [1, 5, 10, 10, 5, 1]
