class Solution:
    """
    LeetCode 693 — Binary Number with Alternating Bits

    --------------------------------------------------------------------
    Method Used
    --------------------------------------------------------------------
    Bitwise Trick using XOR and Shift:
    - If n has alternating bits, then n XOR (n >> 1) yields a binary number
      consisting of all 1s (e.g. 1010 ^ 0101 = 1111).
    - Check if this XOR result is all 1s using the expression:
          x & (x + 1) == 0

    --------------------------------------------------------------------
    Time Complexity
    --------------------------------------------------------------------
    O(1)
        The number of bitwise operations is constant for integer size.

    --------------------------------------------------------------------
    Space Complexity
    --------------------------------------------------------------------
    O(1)
        Only a few integer variables are used.
    """

    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)        # XOR n with n shifted right by one
        return (x & (x + 1)) == 0


if __name__ == "__main__":
    solver = Solution()
    examples = [5, 7, 10, 11, 1, 2]
    for n in examples:
        print(f"{n} ({bin(n)[2:]}) -> {solver.hasAlternatingBits(n)}")
