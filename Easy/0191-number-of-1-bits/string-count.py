class Solution:
    """
    LeetCode Problem 191: Number of 1 Bits

    Write a function that takes an unsigned integer and returns
    the number of '1' bits (also known as the Hamming weight).

    Example:
        Input:  n = 00000000000000000000000000001011
        Output: 3
        Explanation: The binary representation 00000000000000000000000000001011 
                     has three '1' bits.
    """

    def hammingWeight(self, n: int) -> int:
        """
        Return the number of '1' bits (the Hamming weight) in a 32-bit unsigned integer.

        Args:
            n (int): A 32-bit unsigned integer.

        Returns:
            int: The count of '1' bits in the binary representation of `n`.

        Example:
            >>> s = Solution()
            >>> s.hammingWeight(0b00000000000000000000000000001011)
            3
            >>> s.hammingWeight(0b11111111111111111111111111111101)
            31
        """
        n_string = bin(n)[2:]  # Convert to binary string and remove '0b' prefix
        return n_string.count("1")


if __name__ == "__main__":
    # Example usage
    s = Solution()

    # Example input: 11 (binary 1011)
    n = 0b00000000000000000000000000001011
    print("Input (binary):  ", format(n, "032b"))
    print("Hamming Weight:  ", s.hammingWeight(n))

    # Another test
    n = 0b11111111111111111111111111111101
    print("\nInput (binary):  ", format(n, "032b"))
    print("Hamming Weight:  ", s.hammingWeight(n))
