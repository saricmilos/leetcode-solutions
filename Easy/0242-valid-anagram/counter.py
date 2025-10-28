from collections import Counter


class Solution:
    """
    LeetCode Problem 242: Valid Anagram
    -----------------------------------
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters 
    of another, using all original letters exactly once.

    For example:
        - "anagram" and "nagaram" are anagrams.
        - "rat" and "car" are not.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks whether two strings are anagrams of each other using collections.Counter.

        This method leverages the Counter class, which efficiently counts
        occurrences of each character in a string. If both Counters are equal,
        it means both strings contain identical characters with identical frequencies.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if `t` is an anagram of `s`, otherwise False.

        Example:
            >>> solution = Solution()
            >>> solution.isAnagram("anagram", "nagaram")
            True
            >>> solution.isAnagram("rat", "car")
            False

        Time Complexity:
            O(n), where n is the length of the input strings.
            Building each Counter takes linear time.

        Space Complexity:
            O(1) if the character set is fixed (e.g., only lowercase English letters).
            O(n) in the general case for arbitrary Unicode characters.
        """
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    # ✅ Runnable Example Test Cases
    solution = Solution()

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("aacc", "ccac", False),
        ("", "", True),
    ]

    for s, t, expected in test_cases:
        result = solution.isAnagram(s, t)
        print(f"isAnagram({s!r}, {t!r}) -> {result} | Expected: {expected}")
