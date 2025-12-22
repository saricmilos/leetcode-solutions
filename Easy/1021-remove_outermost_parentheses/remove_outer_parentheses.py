"""
LeetCode 1021 - Remove Outermost Parentheses

This module provides a solution to remove the outermost parentheses
from every primitive substring in a valid parentheses string.

Author: Your Name
Language: Python 3
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        Remove the outermost parentheses of every primitive substring.

        A primitive parentheses string is a non-empty valid string that
        cannot be split into two smaller valid parentheses strings.

        Args:
            s (str): A valid parentheses string.

        Returns:
            str: The string after removing the outermost parentheses
                 from each primitive substring.

        Example:
            Input:  "(()())(())"
            Output: "()()()"
        """
        depth = 0
        result = ""

        for char in s:
            if char == "(":
                depth += 1
                # Add '(' only if it is not the outermost parenthesis
                if depth > 1:
                    result += "("
            else:  # char == ')'
                depth -= 1
                # Add ')' only if it is not the outermost parenthesis
                if depth > 0:
                    result += ")"

        return result


def run_examples() -> None:
    """
    Run sample test cases to demonstrate functionality.
    """
    solution = Solution()
    test_cases = [
        "()()",
        "(()())",
        "(()())(())",
        "((()))"
    ]

    for s in test_cases:
        output = solution.removeOuterParentheses(s)
        print(f"Input: {s} -> Output: {output}")


if __name__ == "__main__":
    run_examples()
