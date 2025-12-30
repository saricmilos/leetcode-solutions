from typing import List

class Solution:
    """
    Solution for LeetCode 1732: Find the Highest Altitude.

    Given a list of net gains between points, this class calculates
    the highest altitude reached starting from altitude 0.
    """

    def largestAltitude(self, gain: List[int]) -> int:
        """
        Calculate the highest altitude reached.

        Args:
            gain (List[int]): List of net gains between consecutive points.

        Returns:
            int: Maximum altitude reached.
        """
        # Initialize altitudes list with starting altitude 0
        altitudes = [0] * (len(gain) + 1)

        # Build running altitude list
        for i in range(len(gain)):
            altitudes[i + 1] = altitudes[i] + gain[i]

        # Return the maximum altitude reached
        return max(altitudes)
