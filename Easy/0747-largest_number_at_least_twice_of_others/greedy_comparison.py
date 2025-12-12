from typing import List

class Solution:
    """
    Finds the index of the largest number in the list that is at least
    twice as large as every other number. Returns -1 if no such number exists.
    """

    def dominantIndex(self, nums: List[int]) -> int:
        max_number = max(nums)
        max_index = nums.index(max_number)
        
        for i, num in enumerate(nums):
            if i != max_index and num * 2 > max_number:
                return -1
        
        return max_index


if __name__ == "__main__":
    solution = Solution()
    examples = [
        [3, 6, 1, 0],
        [1, 2, 3, 4],
        [0, 0, 0, 1]
    ]

    for i, nums in enumerate(examples, 1):
        result = solution.dominantIndex(nums)
        print(f"Example {i}: nums = {nums} -> dominant index = {result}")
