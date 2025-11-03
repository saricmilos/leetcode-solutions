class Solution:
    """
    LeetCode 693 — Binary Number with Alternating Bits

    Determine whether a given positive integer has a binary representation
    with alternating bits (no two adjacent bits are the same).

    --------------------------------------------------------------------
    Method Used
    --------------------------------------------------------------------
    Bitwise Pattern Check (via String Simulation)
    - Convert n to binary string.
    - Compare each adjacent pair of bits.
    - If any two adjacent bits are equal, return False.

    --------------------------------------------------------------------
    Time Complexity
    --------------------------------------------------------------------
    O(log n)
        The binary representation has log₂(n) bits.
    --------------------------------------------------------------------
    Space Complexity
    --------------------------------------------------------------------
    O(log n)
        The binary string requires space proportional to the bit length.
    """

    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        for i in range(1, len(bin_n)):
            if bin_n[i] == bin_n[i - 1]:
                return False
        return True


if __name__ == "__main__":
    solver = Solution()
    examples = [5, 7, 10, 11]
    for n in examples:
        print(f"{n} ({bin(n)[2:]}) -> {solver.hasAlternatingBits(n)}")
