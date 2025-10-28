class Solution:
    """
    LeetCode Problem 258: Add Digits
    --------------------------------
    Given an integer `num`, repeatedly add all its digits until
    the result has only one digit, and return it.

    Example:
        Input: num = 38
        Output: 2
        Explanation: 3 + 8 = 11, 1 + 1 = 2
    """

    def addDigits(self, num: int) -> int:
        """
        Repeatedly sums the digits of an integer until a single-digit result is obtained.

        Args:
            num (int): The input integer.

        Returns:
            int: The single-digit result after repeatedly summing digits.

        Time Complexity:
            O(log₁₀(n)) — Each iteration reduces the number’s magnitude.
        
        Space Complexity:
            O(1) — Uses only constant extra space.
        """
        if num == 0:
            return 0

        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        
        return num


if __name__ == "__main__":
    # ✅ Runnable Example Test Cases
    solution = Solution()

    test_cases = [
        (38, 2),
        (0, 0),
        (9, 9),
        (12345, 6),
        (9999, 9),
    ]

    for num, expected in test_cases:
        result = solution.addDigits(num)
        print(f"addDigits({num}) -> {result} | Expected: {expected}")
