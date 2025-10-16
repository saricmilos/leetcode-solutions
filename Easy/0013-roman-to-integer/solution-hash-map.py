class Solution:
    """
    Solution class for LeetCode Problem 13: Roman to Integer.

    Problem:
    Given a Roman numeral string, convert it to an integer.

    Roman numerals are usually written from largest to smallest, left to right.
    However, if a smaller value appears before a larger value, it is subtracted 
    (IV = 4, IX = 9, XL = 40, etc.).

    Approach:
    - Use a dictionary to map Roman numerals to integer values.
    - Iterate through the string:
        - If the current value is smaller than the next value, subtract it.
        - Otherwise, add it.
    - This ensures subtractive notation is handled correctly.
    
    Time Complexity: O(n), where n = length of the string.
    Space Complexity: O(1).
    """

    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral string to its integer value.

        Args:
            s (str): Roman numeral string.

        Returns:
            int: The integer representation of the Roman numeral.
        """
        roman_arabic = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        arabic_total = 0
        length = len(s)

        for index, roman_current in enumerate(s):
            arabic_current = roman_arabic[roman_current]

            # Look ahead to the next numeral if it exists
            if index + 1 < length:
                arabic_next = roman_arabic[s[index + 1]]
                if arabic_current < arabic_next:
                    arabic_total -= arabic_current
                    continue

            # Otherwise, add the current value
            arabic_total += arabic_current

        return arabic_total


# Example usage
if __name__ == "__main__":
    sol = Solution()
    test_cases = ["III", "LVIII", "MCMXCIV", "IX", "XL"]

    for roman in test_cases:
        print(f"{roman} -> {sol.romanToInt(roman)}")
