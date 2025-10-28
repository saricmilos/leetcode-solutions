class Solution:
    """
    LeetCode Problem 263: Ugly Number
    ---------------------------------
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
    Given an integer n, return True if n is an ugly number, otherwise False.

    Example:
        Input: n = 6
        Output: True
        Explanation: 6 = 2 × 3
    """

    def isUgly(self, n: int) -> bool:
        """
        Determines whether a number is an ugly number.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if `n` is an ugly number, False otherwise.

        Approach:
        ---------
        1. Handle edge case: numbers ≤ 0 are not ugly.
        2. Repeatedly divide `n` by 2, 3, or 5 while possible.
        3. If the final result is 1, then it is an ugly number.

        Time Complexity:
            O(logₙ) — because n is divided by factors (2, 3, or 5) multiple times.

        Space Complexity:
            O(1) — constant space usage.
        """
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1


if __name__ == "__main__":
    # ✅ Runnable Example Test Cases
    solution = Solution()

    test_cases = [
        (6, True),
        (8, True),
        (14, False),
        (1, True),
        (0, False),
        (30, True),
    ]

    for n, expected in test_cases:
        result = solution.isUgly(n)
        print(f"isUgly({n}) -> {result} | Expected: {expected}")
