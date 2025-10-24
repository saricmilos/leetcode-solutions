class Solution:
    """
    LeetCode Problem 191: Number of 1 Bits

    Write a function that takes an unsigned integer and returns
    the number of '1' bits (also known as the Hamming weight).

    Optimized using Brian Kernighan’s Algorithm.
    """

    def hammingWeight(self, n: int) -> int:
        """
        Return the number of '1' bits (the Hamming weight) in a 32-bit unsigned integer.

        This implementation uses Brian Kernighan’s algorithm, which repeatedly clears
        the lowest set bit until the number becomes zero.

        Args:
            n (int): A 32-bit unsigned integer.

        Returns:
            int: The count of '1' bits in `n`.

        Example:
            >>> s = Solution()
            >>> s.hammingWeight(0b00000000000000000000000000001011)
            3
            >>> s.hammingWeight(0b11111111111111111111111111111101)
            31
        """
        count = 0
        while n:
            n &= n - 1  # Removes the lowest set bit
            count += 1
        return count


if __name__ == "__main__":
    # Example usage
    s = Solution()

    # Input: 11 (binary 1011)
    n = 0b00000000000000000000000000001011
    print("Input (binary):  ", format(n, "032b"))
    print("Hamming Weight:  ", s.hammingWeight(n))

    # Another test
    n = 0b11111111111111111111111111111101
    print("\nInput (binary):  ", format(n, "032b"))
    print("Hamming Weight:  ", s.hammingWeight(n))
