"""
prefix_common_array.py

Module to compute the prefix common array of two arrays.

Example:
    >>> from prefix_common_array import Solution
    >>> sol = Solution()
    >>> sol.findThePrefixCommonArray([1,3,2,4], [3,1,2,4])
    [0, 2, 3, 4]
"""

from typing import List

class Solution:
    """
    Solution to find the prefix common array of two arrays.

    Methods
    -------
    findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
        Computes, for each index i, the number of elements that appear in both arrays up to index i.
    """

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Find the prefix common array.

        Parameters
        ----------
        A : List[int]
            First input array.
        B : List[int]
            Second input array of the same length as A.

        Returns
        -------
        List[int]
            Array C where C[i] is the number of elements that appear in both A[:i+1] and B[:i+1].
        """
        C = []
        seen_a = set()
        seen_b = set()

        for i in range(len(A)):
            seen_a.add(A[i])
            seen_b.add(B[i])
            common = seen_a & seen_b  # intersection of sets
            C.append(len(common))

        return C


if __name__ == "__main__":
    # Example usage
    sol = Solution()
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    result = sol.findThePrefixCommonArray(A, B)
    print(f"Array A: {A}")
    print(f"Array B: {B}")
    print(f"Prefix common array: {result}")
