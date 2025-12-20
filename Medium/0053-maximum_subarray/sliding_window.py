"""
LeetCode Problem 53: Maximum Subarray
Find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Approach: Kadane's Algorithm (O(n) time, O(1) space)
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Returns the largest sum of a contiguous subarray.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: Maximum subarray sum.
        """
        if not nums:
            raise ValueError("Input array cannot be empty")
        
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            # Decide whether to start a new subarray or continue the previous one
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

# ---------------------------
# Example usage / test cases
# ---------------------------
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"Input: {nums1}")
    print(f"Maximum Subarray Sum: {solution.maxSubArray(nums1)}")  # Output: 6

    # Test case 2
    nums2 = [1]
    print(f"\nInput: {nums2}")
    print(f"Maximum Subarray Sum: {solution.maxSubArray(nums2)}")  # Output: 1

    # Test case 3
    nums3 = [5,4,-1,7,8]
    print(f"\nInput: {nums3}")
    print(f"Maximum Subarray Sum: {solution.maxSubArray(nums3)}")  # Output: 23
