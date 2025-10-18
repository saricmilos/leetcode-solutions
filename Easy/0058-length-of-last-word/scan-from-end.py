class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Return the length of the last word in a string.

        This method scans the string from the end, skipping trailing spaces, 
        and counts the characters of the last word without splitting the string.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the last word. Returns 0 if no words exist.

        Time Complexity:
            O(n), where n is the length of the string `s`. 
            Each character is checked at most once.

        Space Complexity:
            O(1). No extra space is used besides a few integer variables.
        """
        length = 0
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Count characters in the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


if __name__ == "__main__":
    sol = Solution()

    print(sol.lengthOfLastWord("Hello World"))        # Output: 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
    print(sol.lengthOfLastWord("luffy is still joyboy"))        # Output: 6
    print(sol.lengthOfLastWord(" "))                   # Output: 0
