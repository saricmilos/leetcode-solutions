"""
1769. Minimum Number of Operations to Move All Balls to Each Box
---------------------------------------------------------------

Given a string representing boxes ('0' for empty, '1' for a ball),
compute for each box the minimum number of moves to bring all balls
to that box. Moving a ball one step costs 1.

Author: Your Name
"""

from typing import List


class Solution:
    """
    Solution class for computing minimum moves to bring all balls
    to each box.
    """

    def minOperations(self, boxes: str) -> List[int]:
        """
        Computes the minimum number of operations to move all balls
        to each box.

        Args:
            boxes (str): A string of '0' and '1' representing empty
                         boxes and boxes with balls.

        Returns:
            List[int]: List of minimum moves for each box.
        """
        n = len(boxes)
        answer = [0] * n

        # Left-to-right pass
        balls = 0  # Number of balls seen so far
        moves = 0  # Moves needed to bring balls to current position
        for i in range(n):
            answer[i] += moves
            if boxes[i] == "1":
                balls += 1
            moves += balls

        # Right-to-left pass
        balls = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            if boxes[i] == "1":
                balls += 1
            moves += balls

        return answer


def main():
    """
    Runnable example to demonstrate the solution.
    """
    solution = Solution()
    examples = ["110", "001011", "1001", "11111", "0000"]

    for boxes in examples:
        result = solution.minOperations(boxes)
        print(f"Boxes: {boxes} -> Min moves: {result}")


if __name__ == "__main__":
    main()
