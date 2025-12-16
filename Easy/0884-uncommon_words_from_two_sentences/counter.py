from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        Returns a list of words that appear exactly once across both sentences.
        
        Args:
            s1 (str): First sentence.
            s2 (str): Second sentence.
        
        Returns:
            List[str]: List of uncommon words.
        """
        all_words = s1.split() + s2.split()
        word_counts = Counter(all_words)
        return [word for word, freq in word_counts.items() if freq == 1]


# ------------------- Runnable Example -------------------
if __name__ == "__main__":
    solution = Solution()
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    print(solution.uncommonFromSentences(s1, s2))
    # Output: ['sweet', 'sour']
