from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix string amongst an array of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix. Returns an empty string if none exists.
        """
        if not strs:
            return ""

        common_prefix = ""
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            char = shortest[i]
            # Verify this character across all strings
            if all(s[i] == char for s in strs):
                common_prefix += char
            else:
                break  # stop at the first mismatch

        return common_prefix


if __name__ == "__main__":
    # Example usage
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"])) 
    print(sol.longestCommonPrefix(["dog", "racecar", "car"])) 
