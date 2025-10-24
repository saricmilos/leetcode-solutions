import string

class Solution:
    """
    Given a string `columnTitle` representing the column title as it appears in an Excel sheet,
    return its corresponding column number.

    Example mapping:
        A  -> 1
        B  -> 2
        Z  -> 26
        AA -> 27
        AB -> 28

    The problem is essentially converting a base-26 number (A-Z) to base-10.
    """

    def titleToNumber(self, columnTitle: str) -> int:
        """
        Convert an Excel column title (e.g., 'AB') to its corresponding column number.

        Args:
            columnTitle (str): A string consisting of uppercase English letters ('A'–'Z').

        Returns:
            int: The numeric column index corresponding to the Excel column title.

        Example:
            >>> Solution().titleToNumber("A")
            1
            >>> Solution().titleToNumber("Z")
            26
            >>> Solution().titleToNumber("AA")
            27
            >>> Solution().titleToNumber("AB")
            28

        Time Complexity:
            O(n) — where n is the length of `columnTitle`.
            We iterate through each character once.

        Space Complexity:
            O(1) — uses only a few constant extra variables.
        """
        letters = string.ascii_uppercase
        columnTitle_reversed = columnTitle[::-1]
        column_number = 0

        for index, letter in enumerate(columnTitle_reversed):
            column_number += (26 ** index) * (letters.find(letter) + 1)

        return column_number


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    examples = ["A", "Z", "AA", "AB", "ZY", "FXSHRXW"]
    for col in examples:
        print(f"{col} -> {solution.titleToNumber(col)}")
