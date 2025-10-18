class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of 'needle' in 'haystack' using a sliding window.

        This method checks each substring of 'haystack' of length equal to 'needle' 
        to find a match. If 'needle' is empty, returns 0. If 'needle' is not found, returns -1.

        Args:
            haystack (str): The string to search within.
            needle (str): The substring to search for.

        Returns:
            int: The index of the first occurrence of 'needle', or -1 if not found.
        """
        if not needle:
            return 0
        
        length_haystack, length_needle = len(haystack), len(needle)
        for i in range(length_haystack - length_needle + 1):
            if haystack[i:i + length_needle] == needle:
                return i
        return -1


if __name__ == "__main__":
    # Example usage
    sol = Solution()

    print(sol.strStr("hello", "ll"))    
    print(sol.strStr("aaaaa", "bba"))   
    print(sol.strStr("abc", ""))        
