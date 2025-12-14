class Solution:
    """
    LeetCode 824. Goat Latin

    Converts a sentence to "Goat Latin" using the following rules:
    1. If a word begins with a vowel, append "ma" to the end.
    2. If a word begins with a consonant, move the first letter to the end and then append "ma".
    3. Add one 'a' to the end of each word per its position in the sentence (1-indexed).

    Time Complexity: O(n) where n is the length of the sentence
    Space Complexity: O(n)
    """

    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        goat_latin_sentence = []

        words = sentence.split()
        for i, word in enumerate(words):
            if word[0] in vowels:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word += "a" * (i + 1)
            goat_latin_sentence.append(word)

        return " ".join(goat_latin_sentence)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    sentence1 = "I speak Goat Latin"
    print(sol.toGoatLatin(sentence1))
    # Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    # Example 2
    sentence2 = "The quick brown fox"
    print(sol.toGoatLatin(sentence2))
    # Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa"
