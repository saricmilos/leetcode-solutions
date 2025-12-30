from typing import List

class Solution:
    """
    Solution for LeetCode 724: Find Pivot Index.

    The pivot index is the index where the sum of numbers
    to the left is equal to the sum of numbers to the right.
    """

    def pivotIndex(self, nums: List[int]) -> int:
        """
        Find the pivot index of the list.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: The leftmost pivot index if exists, otherwise -1.
        """
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Right sum is total_sum - left_sum - current number
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num

        return -1
