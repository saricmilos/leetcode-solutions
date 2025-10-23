import string

class Solution:
    """
    LeetCode 168 — Excel Sheet Column Title

    Given an integer column number, convert it to its corresponding Excel column title.

    Example:
        1 -> "A"
        28 -> "AB"
        701 -> "ZY"

    Time Complexity: O(log₍26₎(n))
    Space Complexity: O(1)
    """

    def convertToTitle(self, columnNumber: int) -> str:
        """
        Convert a positive integer to its Excel column title.

        Args:
            columnNumber (int): The Excel column number (1-indexed).

        Returns:
            str: The corresponding Excel column title.
        """
        letters = string.ascii_uppercase
        column_title = []

        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing
            remainder = columnNumber % 26
            column_title.append(letters[remainder])
            columnNumber //= 26

        # Reverse because we construct from least significant letter
        return ''.join(reversed(column_title))


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.convertToTitle(1))     # Output: A
    print("Example 2:", solution.convertToTitle(28))    # Output: AB
    print("Example 3:", solution.convertToTitle(701))   # Output: ZY
    print("Example 4:", solution.convertToTitle(702))   # Output: ZZ
