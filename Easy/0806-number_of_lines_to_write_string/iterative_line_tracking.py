"""
LeetCode 806: Number of Lines To Write String
Description:
    Given a string and widths of letters, calculate the minimum number
    of lines needed to write the string such that each line has at most
    100 units of width, and return the width of the last line.

Techniques used:
- Iterative line tracking: Keep track of the current line width and increment
  the line count when adding a letter exceeds the max width.
- Mapping characters to widths: Use ASCII codes to index into the widths list.
"""

from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        """
        Determine the number of lines and the width of the last line
        needed to write the string 's' with given letter widths.

        Args:
            widths (List[int]): List of widths for lowercase letters 'a' to 'z'.
            s (str): String to write.

        Returns:
            List[int]: [number_of_lines, width_of_last_line]
        """
        number_of_lines = 1
        length_of_last_line = 0

        for letter in s:
            width_of_current_letter = widths[ord(letter) - ord("a")]
            new_length = length_of_last_line + width_of_current_letter

            if new_length > 100:
                number_of_lines += 1
                length_of_last_line = width_of_current_letter
            else:
                length_of_last_line = new_length

        return [number_of_lines, length_of_last_line]


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    
    widths_example = [10]*26  # Each letter width = 10
    s_example = "abcdefghijklmnopqrstuvwxyz"
    
    result = solution.numberOfLines(widths_example, s_example)
    print(f"numberOfLines({s_example}) = {result}")
    # Expected output: [3, 60] (26 letters * 10 units → 3 lines, last line 60)
