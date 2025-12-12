from typing import List
from collections import Counter

class Solution:
    """
    Solution for the Shortest Completing Word problem.

    Problem:
        Given a string `licensePlate` and a list of words, find the shortest word
        in the list that contains all the letters in `licensePlate` (ignoring case
        and non-letter characters) at least as many times as they appear in
        `licensePlate`.

    Approach:
        1. Extract and lowercase letters from `licensePlate`.
        2. Count the frequency of each letter.
        3. For each word in the list, count its letters and check if it meets
           all frequency requirements.
        4. Return the shortest word that satisfies the condition.
    """

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Extract letters and count frequencies
        letters = [c.lower() for c in licensePlate if c.isalpha()]
        letter_freq = Counter(letters)
        
        # Filter words that satisfy all letter requirements
        completing_words = []
        for word in words:
            word_freq = Counter(word.lower())
            if all(word_freq.get(letter, 0) >= count for letter, count in letter_freq.items()):
                completing_words.append(word)
        
        # Return the shortest completing word
        return min(completing_words, key=len)


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    examples = [
        ("1s3 PSt", ["step","steps","stripe","stepple"]),
        ("Ah71752", ["suggest","letter","husband","ashtray","hunting"]),
        ("OgEu755", ["enough","gorgeous","outgun"])
    ]

    for i, (licensePlate, words) in enumerate(examples, 1):
        result = solution.shortestCompletingWord(licensePlate, words)
        print(f"Example {i}: licensePlate = {licensePlate}, shortest completing word = {result}")
