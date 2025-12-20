from typing import List

class Solution:
    """
    Solution for the 'Squares of a Sorted Array' problem.

    Given a sorted integer array `nums`, this class provides a method
    to return a new array containing the squares of each number,
    sorted in non-decreasing order.

    Example:
        Input:  nums = [-4, -1, 0, 3, 10]
        Output: [0, 1, 9, 16, 100]
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Returns a sorted list of squares from the input sorted list.

        Args:
            nums (List[int]): A sorted list of integers.

        Returns:
            List[int]: Sorted list of squared integers.
        """
        squared_nums = []
        left, right = 0, len(nums) - 1

        # Use two-pointer technique to find the largest squares first
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                squared_nums.append(nums[left] ** 2)
                left += 1
            else:
                squared_nums.append(nums[right] ** 2)
                right -= 1

        # Reverse the result to get non-decreasing order
        return squared_nums[::-1]


if __name__ == "__main__":
    # Example test cases
    solution = Solution()

    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [0, 1, 2, 3, 4],
        [-5, -3, -2, -1],
        []
    ]

    for i, nums in enumerate(test_cases, 1):
        print(f"Test case {i}: {nums}")
        print(f"Sorted squares: {solution.sortedSquares(nums)}\n")
