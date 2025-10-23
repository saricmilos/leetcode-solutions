class Solution:
    """
    LeetCode Problem 169 — Majority Element

    Given an integer array `nums`, the majority element is the element that appears
    more than ⌊n / 2⌋ times. You may assume that the majority element always exists
    in the array.

    This implementation uses a dictionary (hash map) to count occurrences of each
    number and returns the key with the maximum count.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Example:
        >>> solution = Solution()
        >>> solution.majorityElement([3, 2, 3])
        3
        >>> solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
        2
    """

    def majorityElement(self, nums: list[int]) -> int:
        """
        Returns the majority element from a list of integers.

        Args:
            nums (list[int]): List of integers containing a majority element.

        Returns:
            int: The majority element in the list.

        Example:
            >>> Solution().majorityElement([1, 1, 2])
            1
        """
        number_counts: dict[int, int] = {}

        for number in nums:
            number_counts[number] = number_counts.get(number, 0) + 1

        # Return the key (number) with the highest occurrence count
        return max(number_counts, key=number_counts.get)


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))           # Output: 3
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
