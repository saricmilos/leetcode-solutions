from typing import Dict


class Solution:
    """
    Determine whether a string `s` follows the same pattern given by `pattern`.

    Problem statement (summary):
        Given a pattern and a string s, return True if s follows the same pattern.
        Here "follow" means there is a bijection between a letter in `pattern`
        and a non-empty word in `s` (words separated by spaces).

    Approach:
        Use two dictionaries to maintain a bijection:
        - `letter_to_word`: maps pattern letters -> words
        - `word_to_letter`: maps words -> pattern letters

        For each pair (letter, word) in parallel:
        - If letter already mapped, ensure it maps to the same word.
        - If word already mapped, ensure it maps to the same letter.
        - Otherwise, establish the new mapping in both dictionaries.

    Time complexity: O(n) where n = number of words in `s` (or len(pattern)).
    Space complexity: O(n) for the dictionaries storing mappings.
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Check whether `s` follows `pattern`.

        Args:
            pattern: A string of single-character pattern letters (e.g. "abba").
            s: A string of words separated by spaces (e.g. "dog cat cat dog").

        Returns:
            True if `s` follows `pattern` (bijection letter <-> word), else False.

        Examples:
            >>> Solution().wordPattern("abba", "dog cat cat dog")
            True
            >>> Solution().wordPattern("abba", "dog cat cat fish")
            False
            >>> Solution().wordPattern("aaaa", "dog dog dog dog")
            True
            >>> Solution().wordPattern("abba", "dog dog dog dog")
            False
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        letter_to_word: Dict[str, str] = {}
        word_to_letter: Dict[str, str] = {}

        for letter, word in zip(pattern, words):
            # Check letter -> word consistency
            if letter in letter_to_word:
                if letter_to_word[letter] != word:
                    return False
            else:
                letter_to_word[letter] = word

            # Check word -> letter consistency
            if word in word_to_letter:
                if word_to_letter[word] != letter:
                    return False
            else:
                word_to_letter[word] = letter

        return True


if __name__ == "__main__":
    # Simple runnable examples (also suitable for quick sanity checks)
    sol = Solution()

    examples = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog dog dog dog", True),
        ("abba", "dog dog dog dog", False),
        ("", "", True),  # edge case: empty pattern and empty s
        ("a", "", False),  # pattern length mismatch
    ]

    for patt, text, expected in examples:
        result = sol.wordPattern(patt, text)
        print(f"pattern={patt!r}, s={text!r} -> {result} (expected: {expected})")
        assert result == expected

    print("All example assertions passed.")
