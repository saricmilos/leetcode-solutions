"""
LeetCode 12 - Integer to Roman

This module provides a solution to convert an integer to a Roman numeral.
The input integer is guaranteed to be in the range 1 to 3999.

Author: Your Name
Language: Python 3
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.

        Args:
            num (int): The integer to convert (1 <= num <= 3999).

        Returns:
            str: The Roman numeral representation of num.

        Example:
            Input: 3
            Output: "III"

            Input: 58
            Output: "LVIII"

            Input: 1994
            Output: "MCMXCIV"
        """
        val_symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = ""

        for value, symbol in val_symbols:
            while num >= value:
                num -= value
                result += symbol

        return result


def run_examples() -> None:
    """
    Run sample test cases to demonstrate functionality.
    """
    solution = Solution()
    test_cases = [3, 4, 9, 58, 1994]

    for num in test_cases:
        roman = solution.intToRoman(num)
        print(f"Input: {num} -> Output: {roman}")


if __name__ == "__main__":
    run_examples()
