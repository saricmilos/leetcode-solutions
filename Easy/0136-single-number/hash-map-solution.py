from typing import List

class Solution:
    """
    LeetCode 136 — Single Number

    Given a non-empty array of integers where every element appears twice except for one,
    this method finds and returns the element that appears only once.

    The algorithm uses a hash map (dictionary) to count the frequency of each number.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> solution = Solution()
        >>> solution.singleNumber([2, 2, 1])
        1
        >>> solution.singleNumber([4, 1, 2, 1, 2])
        4
    """

    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the element that appears only once in the list.

        Args:
            nums (List[int]): List of integers where every number appears twice except one.

        Returns:
            int: The unique element that appears only once.
        """
        number_count = {}
        for number in nums:
            number_count[number] = number_count.get(number, 0) + 1

        for number, count in number_count.items():
            if count == 1:
                return number


if __name__ == "__main__":
    # Example runs
    solution = Solution()
    print("Example 1:", solution.singleNumber([2, 2, 1]))          # Output: 1
    print("Example 2:", solution.singleNumber([4, 1, 2, 1, 2]))    # Output: 4
