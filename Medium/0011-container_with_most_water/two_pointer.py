class Solution:
    def maxArea(self, height):
        """
        Calculate the maximum amount of water a container can store.

        This uses a two-pointer approach:
        - Start with pointers at both ends of the array.
        - At each step, compute the area formed by the two lines.
        - Move the pointer corresponding to the shorter line inward.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
