from typing import Any

class Solution:
    """
    Solution for LeetCode 1281: Subtract the Product and Sum of Digits of an Integer.

    Given an integer n, this class computes the difference between the product
    of its digits and the sum of its digits.
    """

    def subtractProductAndSum(self, n: int) -> int:
        """
        Subtract the sum of digits of n from the product of digits of n.

        Args:
            n (int): The input integer.

        Returns:
            int: The difference between the product and sum of digits.
        """
        digit_product = 1
        digit_sum = 0

        for digit in str(n):
            digit_product *= int(digit)
            digit_sum += int(digit)

        return digit_product - digit_sum


def main() -> None:
    """
    Demonstrates usage of the Solution class with example inputs.
    """
    solution = Solution()

    # Example 1
    n = 234
    result = solution.subtractProductAndSum(n)
    print(f"Input: {n} -> Output: {result}")  # Expected Output: 15

    # Example 2
    n = 4421
    result = solution.subtractProductAndSum(n)
    print(f"Input: {n} -> Output: {result}")  # Expected Output: 21


if __name__ == "__main__":
    main()
