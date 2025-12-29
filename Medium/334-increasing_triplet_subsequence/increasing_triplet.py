from typing import List

class Solution:
    """
    Solution for LeetCode 334: Increasing Triplet Subsequence.

    Determines whether the given list of numbers contains an increasing
    subsequence of length three. 

    The algorithm runs in O(n) time and O(1) space.
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Checks if there exists a triplet (i, j, k) such that
        nums[i] < nums[j] < nums[k] with i < j < k.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            bool: True if an increasing triplet exists, False otherwise.
        """
        first = float("inf")   # Smallest number seen so far
        second = float("inf")  # Second smallest number seen so far

        for num in nums:
            if num <= first:
                # Update smallest number
                first = num
            elif num <= second:
                # Update second smallest number
                second = num
            else:
                # Found a number greater than both first and second
                return True

        return False
