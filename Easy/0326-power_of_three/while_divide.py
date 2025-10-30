class Solution:
    """
    Determine if a given integer `n` is a power of three.

    Problem statement:
        Given an integer `n`, return True if it is a power of three. Otherwise, return False.

    Approach:
        Iterative division approach:
        - If n <= 0, immediately return False (powers of 3 are always positive).
        - While n > 1, divide by 3.
        - If at any point n is not divisible by 3, return False.
        - If we reduce n to 1, it is a power of three.

    Time complexity: O(log3(n)) -- each division reduces n by a factor of 3.
    Space complexity: O(1) -- constant extra space.
    """

    def isPowerOfThree(self, n: int) -> bool:
        """
        Check whether `n` is a power of three.

        Args:
            n: Integer to check.

        Returns:
            True if `n` is a power of three, else False.

        Examples:
            >>> Solution().isPowerOfThree(27)
            True
            >>> Solution().isPowerOfThree(0)
            False
            >>> Solution().isPowerOfThree(-3)
            False
            >>> Solution().isPowerOfThree(9)
            True
        """
        if n <= 0:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3
        return True


if __name__ == "__main__":
    sol = Solution()
    examples = [27, 0, -3, 9, 1, 45]

    for n in examples:
        result = sol.isPowerOfThree(n)
        print(f"{n} -> {result}")

    # Quick assertions
    assert sol.isPowerOfThree(27) == True
    assert sol.isPowerOfThree(0) == False
    assert sol.isPowerOfThree(-3) == False
    assert sol.isPowerOfThree(9) == True
    assert sol.isPowerOfThree(1) == True
    assert sol.isPowerOfThree(45) == False

    print("All example assertions passed.")
