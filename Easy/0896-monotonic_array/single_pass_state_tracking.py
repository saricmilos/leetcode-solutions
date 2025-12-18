from typing import List

class Solution:
    """
    Solution for LeetCode 896: Monotonic Array.
    
    Determines whether a given list of integers is monotonic.
    An array is monotonic if it is either entirely non-increasing
    or non-decreasing.
    """
    
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Check if the input list is monotonic.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            bool: True if the list is monotonic, False otherwise.
        """
        increasing = decreasing = True
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False
            elif nums[i] > nums[i + 1]:
                increasing = False
        
        return increasing or decreasing


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    
    test_cases = [
        [1, 2, 2, 3],
        [6, 5, 4, 4],
        [1, 3, 2],
        [1, 1, 1],
        [5]
    ]
    
    for nums in test_cases:
        print(f"Array: {nums} -> Monotonic: {solution.isMonotonic(nums)}")
