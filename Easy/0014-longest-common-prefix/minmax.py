from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix among a list of strings.

        This implementation uses the property that the longest common prefix 
        of the entire list must also be the common prefix of the lexicographically 
        smallest and largest strings. Therefore, we only need to compare these two.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix. Returns an empty string if no common prefix exists.

        """
        if not strs:
            return ""

        s1, s2 = min(strs), max(strs)
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1

        return s1[:i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: 'fl'
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ''
    print(sol.longestCommonPrefix(["interstellar", "internet", "interval"]))  # Output: 'inte'
