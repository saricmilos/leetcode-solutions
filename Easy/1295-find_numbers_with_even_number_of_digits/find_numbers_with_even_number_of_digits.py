from typing import List

class Solution:
    """
    Solution for LeetCode 1295: Find Numbers with Even Number of Digits.

    Given a list of integers, this class counts how many integers have an even number of digits.
    """

    def findNumbers(self, nums: List[int]) -> int:
        """
        Counts numbers with an even number of digits in the input list.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: Count of integers with even number of digits.
        """
        count = 0
        for number in nums:
            if len(str(number)) % 2 == 0:
                count += 1
        return count


def main() -> None:
    """
    Demonstrates usage of the Solution class with example inputs.
    """
    solution = Solution()

    # Example 1
    nums = [12, 345, 2, 6, 7896]
    result = solution.findNumbers(nums)
    print(f"Input: {nums} -> Output: {result}")  # Expected Output: 2

    # Example 2
    nums = [555, 901, 482, 1771]
    result = solution.findNumbers(nums)
    print(f"Input: {nums} -> Output: {result}")  # Expected Output: 1


if __name__ == "__main__":
    main()
