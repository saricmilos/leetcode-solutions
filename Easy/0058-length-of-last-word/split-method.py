class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Return the length of the last word in a string.

        A word is defined as a substring consisting of non-space characters. 
        Leading, trailing, and multiple spaces between words are ignored.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the last word. Returns 0 if no words exist.

        Time Complexity:
            O(n), where n is the length of the string `s`. 
            This is because `split()` scans the entire string once.

        Space Complexity:
            O(n) in the worst case, due to storing all words in a list returned by `split()`.
        """
        list_of_words = s.split()
        if not list_of_words:
            return 0
        return len(list_of_words[-1])


if __name__ == "__main__":
    sol = Solution()

    print(sol.lengthOfLastWord("Hello World"))        # Output: 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
    print(sol.lengthOfLastWord("luffy is still joyboy"))        # Output: 6
    print(sol.lengthOfLastWord(" "))                   # Output: 0
