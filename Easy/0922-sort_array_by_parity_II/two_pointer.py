"""
Sort Array By Parity II
-----------------------
This module provides a Solution class with a method to rearrange 
an array so that elements at even indices are even, and elements 
at odd indices are odd. The input array contains an equal number 
of even and odd integers.

Example:
    Input:  [4,2,5,7]
    Output: [4,5,2,7]  # even indices have even numbers, odd indices have odd numbers
"""

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """
        Rearrange the array so that even-indexed positions hold even numbers
        and odd-indexed positions hold odd numbers.

        Args:
            nums (List[int]): Array with equal number of even and odd integers.

        Returns:
            List[int]: Rearranged array with correct parity positions.
        """
        even_i, odd_i = 0, 1
        n = len(nums)

        while even_i < n and odd_i < n:
            if nums[even_i] % 2 == 0:
                even_i += 2
            elif nums[odd_i] % 2 != 0:
                odd_i += 2
            else:
                # Swap numbers at wrong positions
                nums[even_i], nums[odd_i] = nums[odd_i], nums[even_i]
                even_i += 2
                odd_i += 2

        return nums


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    test_nums1 = [4, 2, 5, 7]
    print(f"Input:  {test_nums1}")
    print(f"Output: {sol.sortArrayByParityII(test_nums1)}\n")

    # Example 2
    test_nums2 = [2, 3, 1, 4]
    print(f"Input:  {test_nums2}")
    print(f"Output: {sol.sortArrayByParityII(test_nums2)}\n")

    # Example 3
    test_nums3 = [1, 0, 5, 6, 7, 4]
    print(f"Input:  {test_nums3}")
    print(f"Output: {sol.sortArrayByParityII(test_nums3)}")
