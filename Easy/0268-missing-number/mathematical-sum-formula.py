class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        LeetCode 268: Missing Number
        
        Given an array `nums` containing n distinct numbers 
        in the range [0, n], this function returns the missing number.
        
        Approach:
        - Use the arithmetic sum formula: n*(n+1)//2
        - Subtract the sum of elements in `nums` from the expected sum.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
