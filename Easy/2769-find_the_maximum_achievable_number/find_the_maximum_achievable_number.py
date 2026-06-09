"""
LeetCode 2769. Find the Maximum Achievable Number
https://leetcode.com/problems/find-the-maximum-achievable-number/

Difficulty: Easy

Problem
-------
You are given two integers, `num` and `t`. An integer `x` is called
achievable if it can become equal to `num` after applying the following
operation no more than `t` times:

    Increase or decrease `x` by 1, and simultaneously
    increase or decrease `num` by 1.

Return the maximum possible achievable number. It can be proven that there
exists at least one achievable number.

Intuition
---------
Each operation lets `x` move up by 1 while `num` moves down by 1, closing
the gap between them by 2 per step. To maximize `x`, do this for all `t`
operations, which makes the largest reachable value `num + 2 * t`.

Example
-------
    Input:  num = 4, t = 1
    Output: 6
    (x = 6: one operation -> x = 5, num = 5, now equal)

    Input:  num = 3, t = 2
    Output: 7

Constraints
-----------
    1 <= num, t <= 50

Complexity
----------
    Time:  O(1)
    Space: O(1)
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


if __name__ == "__main__":
    solution = Solution()

    assert solution.theMaximumAchievableX(4, 1) == 6
    assert solution.theMaximumAchievableX(3, 2) == 7
    assert solution.theMaximumAchievableX(1, 1) == 3

    print("All test cases passed.")
