from typing import List

class Solution:
    """
    Solution for LeetCode 1389: Create Target Array in the Given Order.

    Builds a target array by inserting each value from nums into the position
    specified by the matching entry in index, processing both lists left to right.

    Technique Used:
    - List insertion at a given index (list.insert shifts later elements right)

    Time Complexity: O(n^2) - each insert may shift up to n existing elements
    Space Complexity: O(n) - the target array holds all n values
    """

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Create the target array by inserting nums[i] at position index[i].

        Args:
            nums (List[int]): The values to place into the target array.
            index (List[int]): The target position for each corresponding value.

        Returns:
            List[int]: The target array built in the given order.
        """
        target = []

        for idx, num in zip(index, nums):
            target.insert(idx, num)

        return target


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]),  # Expected: [0, 4, 1, 3, 2]
        ([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]),  # Expected: [0, 1, 2, 3, 4]
        ([1], [0]),                          # Expected: [1]
    ]

    for nums, index in test_cases:
        result = solution.createTargetArray(nums, index)
        print(f"nums={nums}, index={index} -> {result}")
