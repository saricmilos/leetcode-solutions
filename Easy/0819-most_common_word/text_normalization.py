import string
from collections import Counter
from typing import List


class Solution:
    """
    Solution class for LeetCode 819 – Most Common Word.

    Methods
    -------
    mostCommonWord(paragraph: str, banned: List[str]) -> str
        Returns the most frequent word in the paragraph that is not banned.
    """

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Find the most common non-banned word in a paragraph.

        Parameters
        ----------
        paragraph : str
            Input text containing words, spaces, and punctuation.
        banned : List[str]
            List of words that must be ignored during counting.

        Returns
        -------
        str
            The most frequent word that is not in the banned list.

        Notes
        -----
        - Comparison is case-insensitive.
        - Punctuation is treated as a word separator.
        - Guaranteed by the problem that an answer exists.
        """

        # 1. Normalize case to ensure case-insensitive comparison
        paragraph = paragraph.lower()
        banned = set(word.lower() for word in banned)

        # 2. Replace punctuation with spaces
        #    This avoids merging words like "b.b" -> "bb" (incorrect)
        translator = str.maketrans(
            string.punctuation,
            " " * len(string.punctuation)
        )
        clean_paragraph = paragraph.translate(translator)

        # 3. Split into words and filter out banned ones
        words = [
            word for word in clean_paragraph.split()
            if word not in banned
        ]

        # 4. Count word frequencies
        counter = Counter(words)

        # 5. Return the most common word
        return counter.most_common(1)[0][0]


# ------------------------------------------------------------
# Runnable Examples
# ------------------------------------------------------------
if __name__ == "__main__":
    solution = Solution()

    # Example 1: Basic case
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print(solution.mostCommonWord(paragraph1, banned1))
    # Expected output: "ball"

    # Example 2: Punctuation edge case
    paragraph2 = "a b.b"
    banned2 = []
    print(solution.mostCommonWord(paragraph2, banned2))
    # Expected output: "b"

    # Example 3: Multiple punctuation and mixed case
    paragraph3 = "Wow! Wow? WOW... this is amazing, amazing!"
    banned3 = ["this"]
    print(solution.mostCommonWord(paragraph3, banned3))
    # Expected output: "wow"

    # Example 4: Single word
    paragraph4 = "Hello"
    banned4 = []
    print(solution.mostCommonWord(paragraph4, banned4))
    # Expected output: "hello"
