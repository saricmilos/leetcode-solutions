class Solution:
    """
    LeetCode Problem 258: Add Digits
    --------------------------------
    Compute the repeated sum of digits of a non-negative integer until
    a single-digit result is obtained — without using loops or recursion.
    """

    def addDigits(self, num: int) -> int:
        """
        Digital Root Approach — constant time solution.

        Args:
            num (int): The input non-negative integer.

        Returns:
            int: The single-digit result (digital root).

        Explanation:
        ------------
        - If num == 0, return 0.
        - Otherwise, use the formula: 1 + (num - 1) % 9
          This directly computes the digital root in O(1) time.

        Examples:
        ---------
        addDigits(38) -> 2
        addDigits(0) -> 0
        addDigits(12345) -> 6

        Time Complexity:
            O(1) — constant time, no iteration or recursion.

        Space Complexity:
            O(1) — only uses a few variables.
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


if __name__ == "__main__":
    # ✅ Runnable test cases
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
