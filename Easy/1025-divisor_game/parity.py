"""
LeetCode 1025 - Divisor Game

Problem:
Alice and Bob take turns playing a game, with Alice starting first.
A number n is written on the chalkboard. On each turn, a player must:
  - Choose an integer x with 0 < x < n and n % x == 0.
  - Replace n with n - x.
A player who cannot make a move loses the game.

Return True if and only if Alice wins, assuming both players play optimally.

Technique Used:
- Game theory / parity argument

Key Idea:
The whole game collapses to the parity of n:
  - If n is even, the current player can always subtract x = 1, handing the
    opponent an odd number.
  - If n is odd, every divisor x is odd, so n - x is always even, forcing the
    opponent to receive an even number.
Since 1 (the losing position, no valid x) is odd, the player who keeps handing
out odd numbers wins. Therefore Alice wins exactly when n is even.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        Determines whether Alice wins the divisor game under optimal play.

        :param n: int - The starting number on the chalkboard
        :return: bool - True if Alice wins, otherwise False
        """

        return n % 2 == 0


if __name__ == "__main__":
    # Runnable examples
    solution = Solution()

    test_cases = [
        2,   # True  - Alice picks 1, Bob is stuck with 1
        3,   # False - Alice picks 1, Bob wins with 2
        1,   # False - Alice cannot move
        4,   # True
    ]

    for n in test_cases:
        print(f"n = {n} -> Alice wins: {solution.divisorGame(n)}")
