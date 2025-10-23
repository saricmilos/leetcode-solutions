"""

This module contains a Python implementation of the Boyer-Moore Majority Vote Algorithm,
used to find the majority element in a list of integers.

A "majority element" is defined as the element that appears more than ⌊n / 2⌋ times
in the given array.

Example:
    >>> from solution import Solution
    >>> sol = Solution()
    >>> sol.majorityElement([3, 2, 3])
    3
    >>> sol.majorityElement([2, 2, 1, 1, 1, 2, 2])
    2
"""

from typing import List, Optional


class Solution:
    """A class that provides a method to find the majority element in a list of integers."""

    def majorityElement(self, nums: List[int]) -> Optional[int]:
        """
        Finds the majority element in the given list using the Boyer–Moore Majority Vote Algorithm.

        This algorithm runs in O(n) time and O(1) space.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            Optional[int]: The majority element if one exists; otherwise, None.

        Example:
            >>> Solution().majorityElement([3, 2, 3])
            3
            >>> Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
            2
        """
        count = 0
        candidate = None

        for number in nums:
            if count == 0:
                candidate = number
            count += 1 if number == candidate else -1

        return candidate


if __name__ == "__main__":
    # Example usage and demonstration
    sol = Solution()
    print("Example 1:", sol.majorityElement([3, 2, 3]))  # Output: 3
    print("Example 2:", sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
