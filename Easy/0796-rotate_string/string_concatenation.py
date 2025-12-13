"""
LeetCode 796: Rotate String
Description:
    Check if one string can become another string after any number of rotations.

Techniques used:
- String concatenation: Doubling the original string (s + s) to capture all possible rotations.
- Substring search: Using the 'in' operator to check if the goal string exists in the doubled string.
- Length check: Ensuring both strings are of the same length to avoid false positives.
"""

from typing import Any

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Check if 'goal' can be obtained by rotating 's'.

        Args:
            s (str): The original string.
            goal (str): The target string after rotation.

        Returns:
            bool: True if 'goal' is a rotation of 's', False otherwise.
        """
        return len(s) == len(goal) and goal in s + s


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    
    test_cases = [
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ("a", "a", True),
        ("", "", True),
    ]

    for s, goal, expected in test_cases:
        result = solution.rotateString(s, goal)
        print(f"rotateString({s!r}, {goal!r}) = {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
