class Solution:
    """
    Solution class for LeetCode Problem 9: Palindrome Number.

    Problem:
    Determine whether an integer is a palindrome. 
    An integer is a palindrome when it reads the same backward as forward.

    Approach:
    Convert the integer to a string and check if the string 
    is equal to its reverse.
    This is the simplest approach, though it uses O(n) extra space.
    """

    def isPalindrome(self, x: int) -> bool:
        """
        Check if the given integer is a palindrome.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        string_x = str(x)
        reversed_x = string_x[::-1]  # Reverse the string using slicing
        return string_x == reversed_x


# Example usage
if __name__ == "__main__":
    sol = Solution()

    test_numbers = [121, -121, 76243762, 12321, 0]

    for num in test_numbers:
        print(f"{num} -> {sol.isPalindrome(num)}")

