"""
Rectangle Overlap (LeetCode 836)

This module provides a solution to determine whether two axis-aligned
rectangles overlap. Rectangles are represented as:
[x1, y1, x2, y2]

Technique Used:
- Geometry / Interval Overlap
- Separation Axis Principle (2D)

Two rectangles overlap if they overlap on both the X-axis and Y-axis.

Time Complexity: O(1)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        Determines if two rectangles overlap.

        :param rec1: List[int] - [x1, y1, x2, y2] of first rectangle
        :param rec2: List[int] - [x1, y1, x2, y2] of second rectangle
        :return: bool - True if rectangles overlap, otherwise False
        """

        # Check for separation on the X-axis
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
            return False

        # Check for separation on the Y-axis
        if rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False

        return True


if __name__ == "__main__":
    # Runnable examples
    solution = Solution()

    test_cases = [
        ([0, 0, 2, 2], [1, 1, 3, 3]),   # Overlap
        ([0, 0, 1, 1], [1, 1, 2, 2]),   # Touching edges (no overlap)
        ([0, 0, 2, 2], [2, 0, 4, 2]),   # Touching sides (no overlap)
        ([0, 0, 3, 3], [1, 1, 2, 2])    # Fully contained
    ]

    for rec1, rec2 in test_cases:
        result = solution.isRectangleOverlap(rec1, rec2)
        print(f"rec1={rec1}, rec2={rec2} -> overlap={result}")
