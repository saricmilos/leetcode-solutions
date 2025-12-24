"""
Maximum Substrings With Distinct Start
--------------------------------------

For a given string, returns the maximum number of substrings
that can have distinct starting characters.

Author: Your Name
"""

class Solution:
    def maxDistinct(self, s: str) -> int:
        """
        Returns the maximum number of substrings with distinct
        starting characters.

        Args:
            s (str): Input string

        Returns:
            int: Number of distinct characters in the string
        """
        return len(set(s))


def main():
    """
    Runnable examples demonstrating the solution.
    """
    solution = Solution()

    examples = [
        "abc",
        "aaab",
        "leetcode",
        "aaaa",
        ""
    ]

    for s in examples:
        print(f"Input: '{s}' -> Maximum distinct substrings: {solution.maxDistinct(s)}")


if __name__ == "__main__":
    main()
