class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Check if a list contains any duplicate elements.

        This method leverages the property of Python sets, which store only unique elements.
        By comparing the length of the original list to the length of the set created from it,
        we can determine if there are duplicates: if the lengths differ, at least one duplicate exists.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if any integer appears more than once; False otherwise.

        Example:
            >>> solution = Solution()
            >>> solution.containsDuplicate([1, 2, 3, 1])
            True
            >>> solution.containsDuplicate([1, 2, 3, 4])
            False

        Time Complexity:
            O(n) — Creating a set requires iterating over all elements once.

        Space Complexity:
            O(n) — A set is created to store unique elements.
        """
        return len(nums) != len(set(nums))


# -------------------- Runnable Examples --------------------
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1} -> Contains duplicate? {solution.containsDuplicate(nums1)}")
    # Output: True

    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2} -> Contains duplicate? {solution.containsDuplicate(nums2)}")
    # Output: False

    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3} -> Contains duplicate? {solution.containsDuplicate(nums3)}")
    # Output: True
