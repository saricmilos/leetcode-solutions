"""
LeetCode 125 - Valid Palindrome

This module provides a solution to check whether a given string is a valid palindrome,
considering only alphanumeric characters and ignoring cases.

Author: Your Name
Language: Python 3
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if the input string is a valid palindrome.

        A valid palindrome considers only alphanumeric characters and ignores cases.

        Args:
            s (str): Input string.

        Returns:
            bool: True if s is a palindrome, False otherwise.

        Example:
            Input:  "A man, a plan, a canal: Panama"
            Output: True

            Input:  "race a car"
            Output: False
        """
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_s = "".join(char for char in s if char.isalnum())
        cleaned_s_lower = cleaned_s.lower()

        # Compare string with its reverse
        return cleaned_s_lower == cleaned_s_lower[::-1]


def run_examples() -> None:
    """
    Run sample test cases to demonstrate functionality.
    """
    solution = Solution()
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        " ",
        "0P"
    ]

    for s in test_cases:
        output = solution.isPalindrome(s)
        print(f"Input: {s!r} -> Output: {output}")


if __name__ == "__main__":
    run_examples()
