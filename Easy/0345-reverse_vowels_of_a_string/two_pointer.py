from typing import List

class Solution:
    """
    Reverse only the vowels in a string while keeping the positions of other characters unchanged.

    Problem statement:
        Given a string `s`, reverse only the vowels of the string and return the resulting string.
        Vowels are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).

    Approach:
        - Use the two-pointer technique:
            - `left` starts at the beginning of the string
            - `right` starts at the end of the string
        - Move the pointers until they point to vowels
        - Swap the vowels at `left` and `right`
        - Move the pointers inward and continue until they meet

    Time complexity: O(n), where n = len(s)
    Space complexity: O(n), for converting string to a list
    """

    def reverseVowels(self, s: str) -> str:
        """
        Reverse vowels in the input string `s`.

        Args:
            s: Input string.

        Returns:
            A new string with vowels reversed.

        Examples:
            >>> Solution().reverseVowels("hello")
            'holle'
            >>> Solution().reverseVowels("leetcode")
            'leotcede'
            >>> Solution().reverseVowels("aA")
            'Aa'
        """
        vowels = set("aeiouAEIOU")  # use set for O(1) lookups
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s_list[left] not in vowels:
                left += 1
                continue
            if s_list[right] not in vowels:
                right -= 1
                continue
            # swap vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)


if __name__ == "__main__":
    sol = Solution()
    examples = [
        "hello",
        "leetcode",
        "aA",
        "programming",
        "AEIOU",
        "xyz"
    ]

    for text in examples:
        reversed_vowels = sol.reverseVowels(text)
        print(f"{text} -> {reversed_vowels}")

    # Quick assertions for testing
    assert sol.reverseVowels("hello") == "holle"
    assert sol.reverseVowels("leetcode") == "leotcede"
    assert sol.reverseVowels("aA") == "Aa"
    assert sol.reverseVowels("AEIOU") == "UOIEA"
    assert sol.reverseVowels("xyz") == "xyz"

    print("All example assertions passed.")
