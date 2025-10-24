class Solution:
    """

    Given a 32-bit unsigned integer, reverse its bits and return the result.

    Example:
        Input:  n = 00000010100101000001111010011100
        Output:    00111001011110000010100101000000

    The integer input is treated as an unsigned 32-bit binary value.
    """

    def reverseBits(self, n: int) -> int:
        """
        Reverse bits of a given 32-bit unsigned integer.

        Args:
            n (int): A 32-bit unsigned integer.

        Returns:
            int: The unsigned integer resulting from reversing the bits of `n`.

        Example:
            >>> s = Solution()
            >>> s.reverseBits(0b00000010100101000001111010011100)
            964176192
            >>> bin(964176192)
            '0b111001011110000010100101000000'
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


if __name__ == "__main__":
    # Example usage
    s = Solution()

    # Input in binary form for readability
    n = 0b00000010100101000001111010011100
    print("Input (binary):  ", format(n, "032b"))

    result = s.reverseBits(n)
    print("Output (binary): ", format(result, "032b"))
    print("Output (decimal):", result)
