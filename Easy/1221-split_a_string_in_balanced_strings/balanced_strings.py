# balanced_string_split.py

class Solution:
    """
    Solution for LeetCode 1221: Split a String in Balanced Strings.

    A balanced string has an equal number of 'L' and 'R' characters.
    This class counts the maximum number of balanced substrings in a given string.
    """

    def balancedStringSplit(self, s: str) -> int:
        """
        Counts the maximum number of balanced substrings in the input string.

        Args:
            s (str): Input string consisting of 'L' and 'R' characters.

        Returns:
            int: Number of balanced substrings.
        """
        substrings_count = 0
        r_count = 0
        l_count = 0

        for letter in s:
            if letter == "R":
                r_count += 1
            else:
                l_count += 1

            if r_count == l_count:
                substrings_count += 1
                r_count = l_count = 0

        return substrings_count


def main() -> None:
    """
    Demonstrates usage of the Solution class with example inputs.
    """
    solution = Solution()

    # Example 1
    s = "RLRRLLRLRL"
    result = solution.balancedStringSplit(s)
    print(f"Input: {s} -> Balanced substrings count: {result}")  # Expected Output: 4

    # Example 2
    s = "RLLLLRRRLR"
    result = solution.balancedStringSplit(s)
    print(f"Input: {s} -> Balanced substrings count: {result}")  # Expected Output: 3


if __name__ == "__main__":
    main()
