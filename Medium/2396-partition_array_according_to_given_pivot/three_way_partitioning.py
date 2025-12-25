from typing import List

class Solution:
    """
    Solution for LeetCode 2161: Partition Array According to Given Pivot.

    This class provides a method `pivotArray` that partitions an array into
    three parts based on a pivot value:
        1. Elements less than the pivot
        2. Elements equal to the pivot
        3. Elements greater than the pivot

    The relative order within each group is preserved.
    """

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Partition the array according to the pivot.

        Args:
            nums (List[int]): The input list of integers.
            pivot (int): The pivot value.

        Returns:
            List[int]: A new list with elements partitioned around the pivot.
        """
        smaller = []
        equal = []
        bigger = []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                bigger.append(num)

        return smaller + equal + bigger


if __name__ == "__main__":
    # --- Example test cases ---
    solution = Solution()

    test_cases = [
        ([9, 12, 5, 10, 14, 3, 10], 10),
        ([1, 2, 3, 4, 5], 3),
        ([4, 4, 4, 4], 4),
        ([10, 20, 30, 40], 25),
    ]

    for nums, pivot in test_cases:
        result = solution.pivotArray(nums, pivot)
        print(f"Input: nums={nums}, pivot={pivot}")
        print(f"Partitioned: {result}\n")
