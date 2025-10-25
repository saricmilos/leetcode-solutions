class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Determine if an array contains any duplicate elements.

        Args:
            nums (list[int]): List of integers.

        Returns:
            bool: True if any value appears at least twice; False otherwise.
        """
        count_hashmap = {}

        for number in nums:
            count_hashmap[number] = count_hashmap.get(number, 0) + 1
            if count_hashmap[number] > 1:
                return True  # Found a duplicate early

        return False  # All unique


# -------------------- Runnable Examples --------------------
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1} -> Contains duplicate? {solution.containsDuplicate(nums1)}")
    # Output: True

    # Example 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2} -> Contains duplicate? {solution.containsDuplicate(nums2)}")
    # Output: False

    # Example 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3} -> Contains duplicate? {solution.containsDuplicate(nums3)}")
    # Output: True
