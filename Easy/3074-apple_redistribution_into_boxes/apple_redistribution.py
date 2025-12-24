from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        """
        Determine the minimum number of boxes required to store all apples.

        The strategy is greedy:
        - Sort box capacities in descending order.
        - Use the largest boxes first until the total capacity
          is enough to hold all apples.

        Args:
            apple (List[int]): Number of apples in each pack.
            capacity (List[int]): Capacity of each box.

        Returns:
            int: Minimum number of boxes needed.

        Example:
            >>> Solution().minimumBoxes([1, 3, 2], [4, 3, 1])
            2
        """
        # Sort capacities so we use the largest boxes first
        capacity.sort(reverse=True)

        boxes_used = 0
        total_capacity = 0
        total_apples = sum(apple)

        # Add box capacities until all apples can fit
        for cap in capacity:
            total_capacity += cap
            boxes_used += 1
            if total_capacity >= total_apples:
                return boxes_used

        return boxes_used


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    apple = [1, 3, 2]
    capacity = [4, 3, 1]
    print(solution.minimumBoxes(apple, capacity))  # Output: 2

    # Example 2
    apple = [5, 5, 5]
    capacity = [10, 5, 2]
    print(solution.minimumBoxes(apple, capacity))  # Output: 2
