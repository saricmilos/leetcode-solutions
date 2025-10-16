class Solution:
    """
    Solution class for LeetCode Problem 9: Palindrome Number.

    Approach:
    Reverse half of the number and compare it to the other half.
    This avoids converting the number to a string and uses O(1) space.
    """

    def isPalindrome(self, x: int) -> bool:
        """
        Check if the given integer is a palindrome.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """
        # Negative numbers and numbers ending with 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even-length numbers, x == reversed_half
        # For odd-length numbers, x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

# Example usage
if __name__ == "__main__":
    sol = Solution()
    test_numbers = [121, -121, 10, 12321, 0,123444,531]

    for num in test_numbers:
        print(f"Is {num} palindrome? {sol.isPalindrome(num)}")
