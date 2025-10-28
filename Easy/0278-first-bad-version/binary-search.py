# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        LeetCode 278: First Bad Version
        
        Uses binary search to efficiently find the first bad version.
        The function minimizes the number of API calls to isBadVersion().
        
        Approach:
        - Initialize left = 1, right = n
        - Check the middle version:
          - If it's bad, search the left half (right = middle)
          - If it's good, search the right half (left = middle + 1)
        - When left == right, we've found the first bad version.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 1, n
        
        while left < right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        
        return left
