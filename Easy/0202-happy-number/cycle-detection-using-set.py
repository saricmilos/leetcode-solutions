class Solution:
    """
    Class to determine if a number is a "happy number".
    
    A happy number is defined by the following process:
        - Starting with any positive integer, replace the number by the sum 
          of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), 
          or it loops endlessly in a cycle that does not include 1.
        - If it ends in 1, the number is happy; otherwise, it is not.

    Example:
        >>> sol = Solution()
        >>> sol.isHappy(19)
        True
        >>> sol.isHappy(2)
        False
    """

    def isHappy(self, n: int) -> bool:
        """
        Determines if a number n is a happy number.

        Args:
            n (int): A positive integer.

        Returns:
            bool: True if n is a happy number, False otherwise.
        """
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return True


if __name__ == "__main__":
    import unittest

    class TestHappyNumber(unittest.TestCase):
        def setUp(self):
            self.sol = Solution()

        def test_happy_numbers(self):
            self.assertTrue(self.sol.isHappy(1))
            self.assertTrue(self.sol.isHappy(7))
            self.assertTrue(self.sol.isHappy(19))
            self.assertTrue(self.sol.isHappy(100))

        def test_unhappy_numbers(self):
            self.assertFalse(self.sol.isHappy(2))
            self.assertFalse(self.sol.isHappy(3))
            self.assertFalse(self.sol.isHappy(4))
            self.assertFalse(self.sol.isHappy(20))

    # Run unit tests
    unittest.main()
