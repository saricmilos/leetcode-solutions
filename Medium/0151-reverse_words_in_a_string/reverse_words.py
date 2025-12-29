class Solution:
    """
    Solution for LeetCode 151: Reverse Words in a String.

    Given an input string `s`, this class provides a method to reverse the order
    of words in the string. Words are defined as sequences of non-space characters.
    Multiple spaces are reduced to a single space in the output, and leading/trailing
    spaces are removed.
    """

    def reverseWords(self, s: str) -> str:
        """
        Reverses the words in the input string.

        Args:
            s (str): The input string containing words separated by spaces.

        Returns:
            str: A string with the words in reversed order, separated by a single space.
        """
        # Split the string into words, automatically removing extra spaces
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed words with a single space
        return " ".join(reversed_words)
