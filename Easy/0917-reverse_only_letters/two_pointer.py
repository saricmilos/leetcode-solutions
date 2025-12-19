"""
Reverse Only Letters
--------------------
This module provides a Solution class with a method to reverse only
the letters in a given string, leaving all non-letter characters
in their original positions.

Example:
    Input:  "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCb-a"

    Input:  "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"
"""

import string

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Reverse only the letters in the input string.

        Args:
            s (str): The input string containing letters and possibly non-letters.

        Returns:
            str: A new string where only letters are reversed.
        """
        alphabet = string.ascii_letters
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s_list[left] in alphabet and s_list[right] in alphabet:
                # Swap letters
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            elif s_list[left] not in alphabet:
                left += 1
            elif s_list[right] not in alphabet:
                right -= 1

        return "".join(s_list)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    test_str1 = "a-bC-dEf-ghIj"
    print(f"Input:  {test_str1}")
    print(f"Output: {sol.reverseOnlyLetters(test_str1)}\n")

    # Example 2
    test_str2 = "Test1ng-Leet=code-Q!"
    print(f"Input:  {test_str2}")
    print(f"Output: {sol.reverseOnlyLetters(test_str2)}\n")

    # Example 3
    test_str3 = "123-abc-XYZ!"
    print(f"Input:  {test_str3}")
    print(f"Output: {sol.reverseOnlyLetters(test_str3)}")
