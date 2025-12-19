from typing import List
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        """
        Find the element in an array of size 2N that is repeated N times.

        Parameters
        ----------
        nums : List[int]
            The input array of size 2N, where one element is repeated N times
            and the rest appear exactly once.

        Returns
        -------
        int
            The element that appears N times.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n_times = len(nums) // 2
        nums_counts = Counter(nums)

        for number in nums:
            if nums_counts[number] == n_times:
                return number


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,2,3,3], 3),
        ([2,1,2,5,3,2], 2),
        ([5,1,5,2,5,3,5,4], 5),
    ]

    for nums, expected in test_cases:
        result = solution.repeatedNTimes(nums)
        print(f"Input: {nums} | Output: {result} | Expected: {expected}")
