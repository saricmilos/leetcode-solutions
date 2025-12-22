"""
LeetCode 205 - Isomorphic Strings

This module provides a solution to check whether two strings are isomorphic.
Two strings are isomorphic if the characters in one string can be replaced to get the other,
with a one-to-one mapping between characters.

Author: Your Name
Language: Python 3
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Check if two strings are isomorphic.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if s and t are isomorphic, False otherwise.

        Example:
            Input: s = "egg", t = "add"
            Output: True

            Input: s = "foo", t = "bar"
            Output: False
        """
        s_to_t_map = {}
        t_to_s_map = {}

        for s_char, t_char in zip(s, t):
            # Check mapping from s -> t
            if s_char in s_to_t_map:
                if s_to_t_map[s_char] != t_char:
                    return False
            else:
                s_to_t_map[s_char] = t_char

            # Check mapping from t -> s
            if t_char in t_to_s_map:
                if t_to_s_map[t_char] != s_char:
                    return False
            else:
                t_to_s_map[t_char] = s_char

        return True


def run_examples() -> None:
    """
    Run sample test cases to demonstrate functionality.
    """
    solution = Solution()
    test_cases = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("ab", "aa")
    ]

    for s, t in test_cases:
        output = solution.isIsomorphic(s, t)
        print(f"Input: s={s!r}, t={t!r} -> Output: {output}")


if __name__ == "__main__":
    run_examples()
