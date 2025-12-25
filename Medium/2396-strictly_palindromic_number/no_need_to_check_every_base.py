class Solution:
    """
    Solution for LeetCode Problem 2396: Strictly Palindromic Number.
    
    A number n is strictly palindromic if, for every base b from 2 to n-2,
    the representation of n in base b is a palindrome. 
    
    Mathematical insight: For n >= 4, it's impossible for n to be strictly palindromic.
    """
    
    def isStrictlyPalindromic(self, n: int) -> bool:
        """
        Determine if a number is strictly palindromic.
        
        Args:
            n (int): The number to check.
        
        Returns:
            bool: Always False for n >= 4, as no number satisfies the condition.
        """
        return False


# Example usage
if __name__ == "__main__":
    sol = Solution()
    test_cases = [4, 5, 6, 10, 100]
    for n in test_cases:
        print(f"{n} is strictly palindromic? {sol.isStrictlyPalindromic(n)}")
