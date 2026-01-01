class Solution:
    def maxVowels(self, s, k):
        """
        Returns the maximum number of vowels in any substring of length k.

        Approach:
        - Use a sliding window of size k.
        - Count vowels in the initial window.
        - Slide the window one character at a time:
          remove the left character and add the new right character.
        - Track the maximum vowel count seen.

        Time Complexity:
        - O(n)

        Space Complexity:
        - O(1)
        """

        vowels = set("aeiou")
        current_count = 0

        # Count vowels in the first window
        for char in s[:k]:
            if char in vowels:
                current_count += 1

        max_count = current_count

        # Slide the window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1

            max_count = max(max_count, current_count)

        return max_count
