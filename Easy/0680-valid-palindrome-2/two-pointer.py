from typing import Tuple


class Solution:
    """
    Determine whether a string can become a palindrome after deleting at most one character.

    Method
    ------
    Two-pointer greedy scan:
    - Move two pointers from the ends toward the center while characters match.
    - On first mismatch, check whether the substring obtained by skipping the left
      character or skipping the right character is a palindrome (checked in-place
      using pointers). If either is palindrome, return True; otherwise return False.

    Complexity
    ----------
    Time: O(n)
        The outer scan is O(n). The in-place palindrome check runs at most once and
        is O(n) in the worst case, so total is O(n).
    Space: O(1)
        Only constant extra space is used (no slicing, no new strings).
    """

    def validPalindrome(self, s: str) -> bool:
        """
        Return True if `s` is a palindrome after deleting at most one character.

        Examples
        --------
        >>> Solution().validPalindrome("aba")
        True
        >>> Solution().validPalindrome("abca")
        True   # delete 'c' or 'b'
        >>> Solution().validPalindrome("abc")
        False
        """
        def is_palindrome_range(left: int, right: int) -> bool:
            """Check whether s[left:right+1] is a palindrome using indices (no slicing)."""
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try skipping left or skipping right
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    tests = [
        ("aba", True),
        ("abca", True),    # remove 'c' or 'b'
        ("abc", False),
        ("deeee", True),
        ("", True),
        ("a", True),
    ]

    solver = Solution()
    for s, expected in tests:
        out = solver.validPalindrome(s)
        print(f"{s!r}: {out} (expected: {expected})")
