from typing import List

class Solution:
    """
    Optimized solution for LeetCode 1732: Find the Highest Altitude.

    Uses O(1) extra space.
    """

    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = current_altitude = 0

        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
