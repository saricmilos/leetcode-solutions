"""
LeetCode 804: Unique Morse Code Words
Description:
    Given a list of words, convert each word into Morse code and count
    how many unique Morse code transformations exist.

Techniques used:
- Dictionary mapping: Mapping letters to their Morse code representations.
- String concatenation: Using ''.join() for efficient string building.
- Set: To automatically handle uniqueness of transformations.
"""

from typing import List
import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Convert a list of words into Morse code and return the number
        of unique Morse code transformations.

        Args:
            words (List[str]): List of lowercase words.

        Returns:
            int: Number of unique Morse code transformations.
        """
        # Morse code mapping for lowercase letters
        morse_code = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        letter_morse = dict(zip(string.ascii_lowercase, morse_code))

        # Use a set to store unique transformations
        unique_transformations = set()

        for word in words:
            # Convert each word to its Morse code representation
            transformation = ''.join(letter_morse[letter] for letter in word)
            unique_transformations.add(transformation)

        return len(unique_transformations)


if __name__ == "__main__":
    # Example usage
    solution = Solution()

    test_cases = [
        (["gin", "zen", "gig", "msg"], 2),
        (["a"], 1),
        (["hello", "world"], 2),
        (["abc", "bca", "cab"], 3)
    ]

    for words, expected in test_cases:
        result = solution.uniqueMorseRepresentations(words)
        print(f"uniqueMorseRepresentations({words}) = {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")
