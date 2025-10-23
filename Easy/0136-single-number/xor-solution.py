from typing import List

class Solution:
    """
    LeetCode 136 — Single Number (Optimal XOR Solution)

    Uses XOR properties to find the unique number in linear time and constant space.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Example:
        >>> Solution().singleNumber([2, 2, 1])
        1
        >>> Solution().singleNumber([4, 1, 2, 1, 2])
        4
    """

    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the unique number using bitwise XOR.

        Args:
            nums (List[int]): List of integers where every number appears twice except one.

        Returns:
            int: The unique number.
        """
        result = 0
        for num in nums:
            result ^= num  # XOR accumulates the unique number
        return result


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.singleNumber([2, 2, 1]))          # Output: 1
    print("Example 2:", solution.singleNumber([4, 1, 2, 1, 2]))    # Output: 4
