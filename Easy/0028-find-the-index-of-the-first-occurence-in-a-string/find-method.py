class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of 'needle' in 'haystack'.

        If 'needle' is not found, returns -1. If 'needle' is an empty string,
        returns 0, consistent with the behavior of Python's str.find().

        Args:
            haystack (str): The string to search within.
            needle (str): The substring to search for.

        Returns:
            int: The index of the first occurrence of 'needle', or -1 if not found.
        """
        return haystack.find(needle)


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    print(sol.strStr("hello", "ll"))    # Output: 2
    print(sol.strStr("aaaaa", "bba"))   # Output: -1
    print(sol.strStr("abc", ""))        # Output: 0
