class Solution:
    """
    Solution for LeetCode 231: Power of Two.
    
    Determines if a given integer `n` is a power of two.
    """

    def isPowerOfTwo(self, n: int) -> bool:
        """
        Checks if the input number is a power of two.
        
        Args:
            n (int): The integer to check.
            
        Returns:
            bool: True if `n` is a power of two, False otherwise.
            
        Time Complexity: O(log n) — each division by 2 reduces n by half.
        Space Complexity: O(1) — only constant extra space is used.
        """
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2

        return True


if __name__ == "__main__":
    sol = Solution()

    # Runnable examples
    test_cases = [1, 2, 3, 4, 16, 218]
    for n in test_cases:
        print(f"isPowerOfTwo({n}) -> {sol.isPowerOfTwo(n)}")
