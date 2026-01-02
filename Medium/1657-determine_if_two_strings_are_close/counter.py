from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Determine whether two strings are close.

        Two strings are considered close if:
        1. They have the same length.
        2. They contain the same set of characters.
        3. The frequency distribution of characters is identical,
           regardless of which character has which frequency.

        :param word1: First input string
        :param word2: Second input string
        :return: True if the strings are close, otherwise False
        """
        # Lengths must match
        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Both strings must contain the same characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Frequency distributions must match
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True
