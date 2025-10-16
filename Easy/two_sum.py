from typing import List

class Solution:
    """
    Solution class for LeetCode Two Sum problem.
    
    Problem:
    Given an array of integers `nums` and an integer `target`, return the indices 
    of the two numbers such that they add up to `target`. You may assume that each 
    input would have exactly one solution, and you may not use the same element twice. 
    The answer can be returned in any order.

    Approach:
    This implementation uses a hash map (dictionary) to store numbers and their indices 
    while iterating through the array. For each number, it checks if the complement 
    (target - number) already exists in the dictionary. If found, the indices are returned. 
    This approach has O(n) time complexity and O(n) space complexity.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices in `nums` such that the numbers at those indices add up to `target`.

        Args:
            nums (List[int]): List of integers.
            target (int): Target sum.

        Returns:
            List[int]: Indices of the two numbers adding up to target.
        """
        # Dictionary to store number -> index mapping
        number_index = {}

        # Iterate over the array with index
        for index, number in enumerate(nums):
            complement = target - number  # The number needed to reach the target
            if complement in number_index:
                # Found the two numbers; return their indices
                return [number_index[complement], index]
            # Store the current number with its index
            number_index[number] = index

# Example usage
if __name__ == "__main__":
    # Create an instance of Solution
    sol = Solution()

    # Example input
    nums = [24, 7, 18 ,11,1442141, 2, 15]
    target = 9

    # Call the twoSum method and print result
    print(sol.twoSum(nums, target))  # Output: [0, 1]
