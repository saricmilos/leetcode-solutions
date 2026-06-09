"""
LeetCode 2235. Add Two Integers
https://leetcode.com/problems/add-two-integers/

Difficulty: Easy

Problem
-------
Given two integers `num1` and `num2`, return the sum of the two integers.

Example
-------
    Input:  num1 = 12, num2 = 5
    Output: 17

Constraints
-----------
    -100 <= num1, num2 <= 100

Complexity
----------
    Time:  O(1)
    Space: O(1)
"""


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


if __name__ == "__main__":
    solution = Solution()

    # Basic sanity checks
    assert solution.sum(12, 5) == 17
    assert solution.sum(-10, 4) == -6
    assert solution.sum(0, 0) == 0

    print("All test cases passed.")