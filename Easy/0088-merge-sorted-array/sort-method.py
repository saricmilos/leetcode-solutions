from typing import List

class Solution:
    """
    Simple merge solution for LeetCode 88: Merge Sorted Array
    
    This approach copies elements from nums2 into the empty space at the end of nums1,
    then sorts nums1 to produce the final merged sorted array.

    Time Complexity: O((m + n) log(m + n)) due to sorting
    Space Complexity: O(1) extra space (in-place)
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place by copying and sorting.
        
        Args:
            nums1 (List[int]): First sorted array with extra space at the end
            m (int): Number of valid elements in nums1
            nums2 (List[int]): Second sorted array
            n (int): Number of elements in nums2
        
        Returns:
            None: Modifies nums1 in-place
        """
        # Copy nums2 elements into the extra space at the end of nums1
        for index, number in enumerate(nums2):
            nums1[m + index] = number  # fill starting from index m

        # Sort nums1 to get the final merged array
        nums1.sort()


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
