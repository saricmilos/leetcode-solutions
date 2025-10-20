from typing import List

class Solution:
    """
    Optimized in-place merge for LeetCode 88: Merge Sorted Array.

    This implementation merges two sorted arrays, nums1 and nums2, into nums1 in-place
    using a three-pointer approach from the end. This avoids extra space and unnecessary sorting.

    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place.

        Args:
            nums1 (List[int]): First sorted array with extra space at the end
            m (int): Number of valid elements in nums1
            nums2 (List[int]): Second sorted array
            n (int): Number of elements in nums2

        Returns:
            None: nums1 is modified in-place
        """
        pointer1, pointer2, pointer3 = m - 1, n - 1, m + n - 1

        # Merge from the end to avoid overwriting elements in nums1
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
            pointer3 -= 1

        # If nums2 still has elements, copy them
        while pointer2 >= 0:
            nums1[pointer3] = nums2[pointer2]
            pointer2 -= 1
            pointer3 -= 1


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1,2,2,3,5,6]

    # Example 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    sol.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1]

    # Example 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    sol.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1]
