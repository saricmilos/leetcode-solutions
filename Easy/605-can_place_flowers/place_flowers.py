from typing import List

class Solution:
    """
    LeetCode 605 - Can Place Flowers

    This solution determines whether it is possible to plant `n` new flowers
    in a flowerbed without violating the rule that no two flowers can be
    adjacent. The flowerbed is represented as a list where:
    - 0 indicates an empty plot
    - 1 indicates a planted flower
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determines if `n` flowers can be planted in the flowerbed.

        Args:
            flowerbed (List[int]): The flowerbed represented as a binary list.
            n (int): Number of flowers to plant.

        Returns:
            bool: True if `n` flowers can be planted, False otherwise.
        """
        planted = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    planted += 1

                    if planted >= n:
                        return True

        return planted >= n
