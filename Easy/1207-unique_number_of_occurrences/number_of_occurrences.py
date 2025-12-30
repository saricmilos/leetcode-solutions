from typing import List

class Solution:
    """
    Solution for LeetCode 1207: Unique Number of Occurrences.

    Determines whether the number of occurrences of each value in the array is unique.
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Check if the number of occurrences of each element is unique.

        Args:
            arr (List[int]): List of integers.

        Returns:
            bool: True if occurrences are unique, False otherwise.
        """
        # Count occurrences
        occ = {}
        for num in arr:
            occ[num] = occ.get(num, 0) + 1

        # Check uniqueness of occurrence counts
        values = list(occ.values())
        return len(values) == len(set(values))
