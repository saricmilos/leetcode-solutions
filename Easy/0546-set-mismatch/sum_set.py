class Solution:
    """
    LeetCode 645: Set Mismatch
    --------------------------
    Given an integer array `nums` containing numbers from 1 to n:
      - One number is duplicated
      - One number is missing
    The goal is to return a list [duplicate, missing].
    """

    def findErrorNums(self, nums: list[int]) -> list[int]:
        """
        Finds the duplicated and missing numbers in the given list.

        Approach:
        - Use set operations to identify the missing number by comparing
          the expected sum (1..n) with the sum of unique numbers.
        - Identify the duplicate number by comparing the total sum with
          the unique sum.

        Args:
            nums (list[int]): List of integers containing numbers from 1 to n
                              with one number duplicated and one missing.

        Returns:
            list[int]: A list containing two integers [duplicate, missing].

        Example:
            >>> s = Solution()
            >>> s.findErrorNums([1, 2, 2, 4])
            [2, 3]

        Time Complexity:
            O(n) — Single pass through nums, with O(n) for set and sum operations.

        Space Complexity:
            O(n) — Due to use of an auxiliary set.
        """
        n = len(nums)
        full_set = set(range(1, n + 1))
        nums_set = set(nums)

        # Calculate missing and duplicate
        missing_number = sum(full_set) - sum(nums_set)
        duplicated_number = sum(nums) - sum(nums_set)

        return [duplicated_number, missing_number]


# ---------------------------
# Example usage (runnable)
# ---------------------------
if __name__ == "__main__":
    s = Solution()
    print(s.findErrorNums([1, 2, 2, 4]))  # Output: [2, 3]
    print(s.findErrorNums([3, 2, 3, 4, 6, 5]))  # Output: [3, 1]
