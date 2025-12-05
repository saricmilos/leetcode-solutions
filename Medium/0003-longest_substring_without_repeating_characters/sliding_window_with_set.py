class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        LeetCode 3 — Longest Substring Without Repeating Characters
        -----------------------------------------------------------
        Given a string s, find the length of the longest substring 
        without repeating characters.

        Approach:
        Uses a sliding window with a set to track seen characters.
        Expands the window using the right pointer, and shrinks it 
        when a duplicate character is found. Tracks the maximum 
        window size during the traversal.

        Time Complexity:  O(n)
        Space Complexity: O(min(n, k))   # k = charset size
        """

        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If character already in current window, shrink from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add new character to the window
            char_set.add(s[right])

            # Update maximum window size
            max_len = max(max_len, right - left + 1)

        return max_len


# -----------------------------
# Example Usage (Runnable)
# -----------------------------
if __name__ == "__main__":
    solution = Solution()

    examples = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "au",
        "dvdf"
    ]

    for s in examples:
        print(f"Input:  {s}")
        print(f"Output: {solution.lengthOfLongestSubstring(s)}")
        print("-" * 40)
