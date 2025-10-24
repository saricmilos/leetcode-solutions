class Solution:
    """
    Reverse bits of a given 32-bit unsigned integer.
    """

    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.

        Args:
            n (int): Input integer (0 ≤ n < 2^32)

        Returns:
            int: Integer whose binary representation is the reversed bits of n.

        Example:
            >>> Solution().reverseBits(43261596)
            964176192
            # Explanation:
            # 43261596  -> 00000010100101000001111010011100
            # reversed  -> 00111001011110000010100101000000
            # = 964176192

        Time Complexity:
            O(1) — We process 32 bits (constant).

        Space Complexity:
            O(1)
        """
        n_binary = bin(n)[2:].zfill(32)     # Get 32-bit binary representation
        reversed_binary = n_binary[::-1]    # Reverse the bits
        return int(reversed_binary, 2)      # Convert back to integer


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596))  # Expected output: 964176192
    print(sol.reverseBits(4294967293))  # Expected output: 3221225471
