class Solution:
    """
    LeetCode 657: Robot Return to Origin
    ------------------------------------
    The robot starts at (0, 0) and moves based on a sequence of characters:
      'U' = up, 'D' = down, 'L' = left, 'R' = right.
    Determine whether the robot returns to the origin after all moves.
    """

    def judgeCircle(self, moves: str) -> bool:
        """
        Checks if the robot returns to the origin using count-based movement balance.

        Args:
            moves (str): String of moves containing 'U', 'D', 'L', 'R'.

        Returns:
            bool: True if the robot returns to (0, 0), else False.

        Example:
            >>> s = Solution()
            >>> s.judgeCircle("UD")
            True
            >>> s.judgeCircle("LL")
            False

        Time Complexity:
            O(n) — Each count() call scans the string once.

        Space Complexity:
            O(1) — Only a few integer variables are used.
        """
        moves_up_down = moves.count("U") - moves.count("D")
        moves_right_left = moves.count("L") - moves.count("R")
        return moves_up_down == 0 and moves_right_left == 0


# ---------------------------
# Example usage (runnable)
# ---------------------------
if __name__ == "__main__":
    s = Solution()
    print(s.judgeCircle("UD"))   # True — returns to origin
    print(s.judgeCircle("LL"))   # False — ends left of origin
    print(s.judgeCircle("URDL")) # True — full loop
