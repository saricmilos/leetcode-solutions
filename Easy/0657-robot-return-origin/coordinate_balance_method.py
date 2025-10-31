class Solution:
    """
    LeetCode 657: Robot Return to Origin
    ------------------------------------
    The robot starts at the origin point (0, 0) on a 2D plane.
    Given a sequence of moves containing the characters:
        'U' (up), 'D' (down), 'L' (left), and 'R' (right),
    determine whether the robot returns to the origin after completing all moves.
    """

    def judgeCircle(self, moves: str) -> bool:
        """
        Determines if the robot returns to the origin after executing a series of moves.

        Args:
            moves (str): A string consisting of characters 'U', 'D', 'L', and 'R'.

        Returns:
            bool: True if the robot returns to (0, 0), otherwise False.

        Example:
            >>> s = Solution()
            >>> s.judgeCircle("UD")
            True
            >>> s.judgeCircle("LL")
            False

        Time Complexity:
            O(n) — we iterate once through all moves.

        Space Complexity:
            O(1) — uses only constant extra space.
        """
        moves_up_down = 0
        moves_right_left = 0

        for move in moves:
            if move == "U":
                moves_up_down += 1
            elif move == "D":
                moves_up_down -= 1
            elif move == "L":
                moves_right_left += 1
            elif move == "R":
                moves_right_left -= 1

        return moves_up_down == 0 and moves_right_left == 0


# ---------------------------
# Example usage (runnable)
# ---------------------------
if __name__ == "__main__":
    s = Solution()
    print(s.judgeCircle("UD"))   # True — back to origin
    print(s.judgeCircle("LL"))   # False — stays left
    print(s.judgeCircle("URDL")) # True — full loop
