class Solution:
    """
    Solution for LeetCode Problem 66: Plus One.

    Given a non-empty array of decimal digits representing a non-negative integer, 
    increment one to the integer. The digits are stored such that the most significant 
    digit is at the head of the list, and each element contains a single digit. 
    You may assume the integer does not contain any leading zero, except the number 0 itself.

    Approach:
        1. Iterate through the list from the last digit to the first.
        2. If a digit is less than 9, increment it by 1 and return the list immediately.
        3. If a digit is 9, set it to 0 and carry over the addition to the next significant digit.
        4. If all digits are 9, prepend 1 to the list to handle the carryover.

    Time Complexity:
        O(n), where n is the number of digits in the input list. 
        In the worst case, we may need to traverse all digits (e.g., [9,9,9]).

    Space Complexity:
        O(1) extra space (ignoring input/output), except in the worst-case when all digits are 9, 
        where we create a new list with length n+1.
    """

    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


if __name__ == "__main__":
    # Instantiate the solution class
    solution = Solution()
    
    # Example test cases
    test_cases = [
        [1, 2, 3],   # Normal case
        [4, 3, 2, 1], # Normal case
        [9, 9, 9],    # All digits are 9
        [0],          # Single zero
        [1, 9, 9]     # Mixed carry
    ]
    
    # Run and print results
    for digits in test_cases:
        result = solution.plusOne(digits.copy()) 
        print(f"Input: {digits} -> Output: {result}")
