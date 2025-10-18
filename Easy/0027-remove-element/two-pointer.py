class Solution:
    def removeElement(self, nums, val):
        """
        Remove all occurrences of a specified value from a list in-place.

        This method modifies the input list so that the first 'k' elements 
        contain the values not equal to 'val'. The remaining elements beyond 
        'k' are not guaranteed to hold any specific values.

        Args:
            nums (List[int]): The input list of integers.
            val (int): The value to remove from the list.

        Returns:
            int: The number of elements in the list that are not equal to 'val'.
        """
        if not nums:
            return 0
        
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    nums1 = [3, 2, 2, 3]
    k1 = sol.removeElement(nums1, 3)
    print(k1)          # Output: 2
    print(nums1[:k1])  # Output: [2, 2]

    nums2 = [0,1,2,2,3,0,4,2]
    k2 = sol.removeElement(nums2, 2)
    print(k2)          # Output: 5
    print(nums2[:k2])  # Output: [0, 1, 3, 0, 4]
