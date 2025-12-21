from typing import List

class Solution:
    """
    Solution for LeetCode 1051: Height Checker.

    Given a list of student heights, counts how many are not in the expected
    non-decreasing order.
    """

    def heightChecker(self, heights: List[int]) -> int:
        """
        Counts the number of indices where the current height differs from
        the expected sorted order.

        Args:
            heights (List[int]): List of student heights.

        Returns:
            int: Number of students out of order.
        """
        expected = sorted(heights)
        count = 0

        for h, e in zip(heights, expected):
            if h != e:
                count += 1

        return count


def main() -> None:
    """
    Demonstrates usage of the Solution class with example inputs.
    """
    solution = Solution()

    # Example 1
    heights = [1, 1, 4, 2, 1, 3]
    result = solution.heightChecker(heights)
    print(f"Input: {heights} -> Output: {result}")  # Expected Output: 3

    # Example 2
    heights = [5, 1, 2, 3, 4]
    result = solution.heightChecker(heights)
    print(f"Input: {heights} -> Output: {result}")  # Expected Output: 5


if __name__ == "__main__":
    main()
