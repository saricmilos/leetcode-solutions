"""
LeetCode 1822. Sign of the Product of an Array
https://leetcode.com/problems/sign-of-the-product-of-an-array/

Difficulty: Easy

Problem
-------
There is a function `signFunc(x)` that returns:

    1   if x is positive
   -1   if x is negative
    0   if x is equal to 0

You are given an integer array `nums`. Let `product` be the product of all
values in `nums`. Return `signFunc(product)`.

Intuition
---------
The magnitude of the product never matters, only its sign, so there is no
need to actually multiply the values (which could overflow into a huge
number). The sign is decided by two facts alone:

    * If any element is 0, the product is 0.
    * Otherwise the product is negative when the count of negative numbers
      is odd, and positive when it is even.

So a single pass that bails out on a zero and counts negatives is enough.

Example
-------
    Input:  nums = [-1, -2, -3, -4, 3, 2, 1]
    Output: 1
    (product = 144, which is positive)

    Input:  nums = [1, 5, 0, 2, -3]
    Output: 0
    (product = 0)

    Input:  nums = [-1, 1, -1, 1, -1]
    Output: -1
    (product = -1)

Constraints
-----------
    1 <= nums.length <= 1000
    -100 <= nums[i] <= 100

Complexity
----------
    Time:  O(n)  - single pass over nums
    Space: O(1)  - only a counter is kept
"""

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negatives += 1

        return 1 if negatives % 2 == 0 else -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
    assert solution.arraySign([1, 5, 0, 2, -3]) == 0
    assert solution.arraySign([-1, 1, -1, 1, -1]) == -1
    assert solution.arraySign([1]) == 1

    print("All test cases passed.")
