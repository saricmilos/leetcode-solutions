class Solution:
    """
    LeetCode Problem 258: Add Digits
    --------------------------------
    Given a non-negative integer `num`, repeatedly add all its digits
    until the result has only one digit, and return it.

    Example:
        Input: num = 38
        Output: 2
        Explanation: 3 + 8 = 11, 1 + 1 = 2
    """

    def addDigits(self, num: int) -> int:
        """
        Recursively sums the digits of an integer until a single-digit result is obtained.

        Args:
            num (int): The input non-negative integer.

        Returns:
            int: The single-digit result after recursive summation.

        Approach:
        ---------
        1. Base Case:
            If num < 10, it is already a single-digit number.
            Return num directly. This stops the recursion.
        
        2. Recursive Case:
            - Compute the sum of all digits in `num`.
            - Call `addDigits` recursively on this sum.
            - The final return value propagates back up through all recursive calls.

        Example Execution:
        ------------------
        Input: 38

        Call 1: addDigits(38)
            - num >= 10 → sum digits: 3 + 8 = 11
            - return addDigits(11)

        Call 2: addDigits(11)
            - num >= 10 → sum digits: 1 + 1 = 2
            - return addDigits(2)

        Call 3: addDigits(2)
            - num < 10 → return 2

        Final Output: 2 (propagates back through Call 2 → Call 1 → original call)

        Time Complexity:
            O(log₁₀(n)) — Each recursive call reduces the number by roughly a factor of 10.
        
        Space Complexity:
            O(log₁₀(n)) — Due to the recursion call stack.
        """
        # Base case
        if num < 10:
            return num

        # Recursive case: sum digits and recurse
        digit_sum = sum(int(digit) for digit in str(num))
        return self.addDigits(digit_sum)


if __name__ == "__main__":
    # ✅ Runnable Example Test Cases
    solution = Solution()

    test_cases = [
        (38, 2),
        (0, 0),
        (9, 9),
        (12345, 6),
        (9999, 9),
    ]

    for num, expected in test_cases:
        result = solution.addDigits(num)
        print(f"addDigits({num}) -> {result} | Expected: {expected}")
