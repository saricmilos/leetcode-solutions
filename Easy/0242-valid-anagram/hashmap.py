class Solution:
    """
    LeetCode Problem 242: Valid Anagram
    -----------------------------------
    Given two strings `s` and `t`, determine if `t` is an anagram of `s`.
    
    An anagram is a word or phrase formed by rearranging the letters of a 
    different word or phrase, typically using all the original letters exactly once.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks whether two strings are anagrams of each other.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if `t` is an anagram of `s`, False otherwise.

        Time Complexity:
            O(n), where n is the length of the strings `s` and `t`.
            We iterate through each string once to build frequency maps.

        Space Complexity:
            O(1) if we assume a fixed alphabet (e.g., lowercase English letters),
            otherwise O(n) in the general case for arbitrary Unicode characters.
        """
        if len(s) != len(t):
            return False

        hashmap_s = {}
        hashmap_t = {}

        for letter in s:
            hashmap_s[letter] = hashmap_s.get(letter, 0) + 1

        for letter in t:
            hashmap_t[letter] = hashmap_t.get(letter, 0) + 1

        return hashmap_s == hashmap_t


if __name__ == "__main__":
    # ✅ Runnable Example Test Cases
    solution = Solution()

    print(solution.isAnagram("anagram", "nagaram"))  # Expected: True
    print(solution.isAnagram("rat", "car"))          # Expected: False
    print(solution.isAnagram("listen", "silent"))    # Expected: True
    print(solution.isAnagram("aacc", "ccac"))        # Expected: False
