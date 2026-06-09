"""
LeetCode 1929. Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/

Difficulty: Easy

Problem
-------
Given an integer array `nums` of length `n`, build an array `ans` of length
`2 * n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for
`0 <= i < n`. In other words, `ans` is the concatenation of `nums` with
itself. Return `ans`.

Example
-------
    Input:  nums = [1, 2, 1]
    Output: [1, 2, 1, 1, 2, 1]

    Input:  nums = [1, 3, 2, 1]
    Output: [1, 3, 2, 1, 1, 3, 2, 1]

Constraints
-----------
    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000

Complexity
----------
    Time:  O(n)  - single pass over nums
    Space: O(n)  - the result array holds 2 * n elements
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = 2 * n * [0]

        # Place each value at index i and again at index i + n.
        for i in range(n):
            ans[i], ans[i + n] = nums[i], nums[i]

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert solution.getConcatenation([7]) == [7, 7]

    print("All test cases passed.")
