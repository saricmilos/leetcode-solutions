class Solution:
    def searchInsert(self, nums, target):
        """
        Find the index at which a target value should be inserted in a sorted list.

        Uses binary search to efficiently locate the target. If the target exists
        in the list, returns its index. If not, returns the index where it would
        be inserted to maintain the list's sorted order.

        Args:
            nums (List[int]): A list of integers sorted in ascending order.
            target (int): The value to search for.

        Returns:
            int: The index of the target if found, or the insertion position if not found.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    nums1 = [1, 3, 5, 6]
    print(sol.searchInsert(nums1, 5))  # Output: 2
    print(sol.searchInsert(nums1, 2))  # Output: 1
    print(sol.searchInsert(nums1, 7))  # Output: 4
    print(sol.searchInsert(nums1, 0))  # Output: 0
