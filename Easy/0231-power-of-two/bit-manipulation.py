class Solution:
    """
    Solution for LeetCode 231: Power of Two using bit manipulation.
    
    A number is a power of two if it has exactly one '1' bit in its binary representation.
    For example:
        1 -> 0b1
        2 -> 0b10
        4 -> 0b100
        8 -> 0b1000

    Key Idea:
    -----------------
    If n is a power of two:
        n & (n - 1) == 0
    Why?
        - Subtracting 1 from n flips all bits after the rightmost 1 (including that 1):
            Example: n = 8 -> 0b1000
                     n - 1 = 7 -> 0b0111
                     n & (n - 1) = 0b1000 & 0b0111 = 0
        - If n has more than one '1' bit, n & (n - 1) will not be zero.
        - Works only for positive numbers (n > 0).

    Time Complexity: O(1) — single bitwise operation.
    Space Complexity: O(1) — uses constant extra space.
    """

    def isPowerOfTwo(self, n: int) -> bool:
        """
        Checks if the input number is a power of two using bit manipulation.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if `n` is a power of two, False otherwise.
        """
        return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    sol = Solution()
    
    # Runnable examples
    test_cases = [1, 2, 3, 4, 16, 218]
    for n in test_cases:
        print(f"isPowerOfTwo({n}) -> {sol.isPowerOfTwo(n)}")
