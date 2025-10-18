class Solution:
    def removeDuplicates(self, nums):
        """
        Remove duplicates from a sorted list in-place.

        This method modifies the input list so that the first 'k' elements 
        contain the unique values in their original order. The rest of the 
        list beyond 'k' is not guaranteed to hold any particular values.

        Args:
            nums (List[int]): A list of integers sorted in non-decreasing order.

        Returns:
            int: The number of unique elements in the list.
        """
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(k1)          
    print(nums1[:k1])  

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(k2)          
    print(nums2[:k2])  
