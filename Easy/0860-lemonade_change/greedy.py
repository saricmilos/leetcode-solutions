"""
LeetCode 860 - Lemonade Change

Problem:
You are running a lemonade stand where each lemonade costs $5.
Customers pay with $5, $10, or $20 bills in the given order.
You must provide correct change to each customer.

Return True if you can provide correct change to every customer,
otherwise return False.

Technique Used:
- Greedy Algorithm
- Counter-based simulation

Key Idea:
Always give change in a way that preserves smaller bills ($5) for future customers.
When handling a $20 bill, prioritize giving $10 + $5 over three $5 bills.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Determines whether correct change can be provided to all customers.

        :param bills: List[int] - Bills paid by customers in order
        :return: bool - True if correct change can be given, otherwise False
        """

        five_bills = 0
        ten_bills = 0

        for bill in bills:
            if bill == 5:
                five_bills += 1

            elif bill == 10:
                if five_bills == 0:
                    return False
                five_bills -= 1
                ten_bills += 1

            elif bill == 20:
                # Prefer using $10 + $5 for change
                if ten_bills > 0 and five_bills > 0:
                    ten_bills -= 1
                    five_bills -= 1
                # Otherwise, use three $5 bills
                elif five_bills >= 3:
                    five_bills -= 3
                else:
                    return False

        return True


if __name__ == "__main__":
    # Runnable examples
    solution = Solution()

    test_cases = [
        [5, 5, 5, 10, 20],      # True
        [5, 5, 10],            # True
        [10, 10],              # False
        [5, 5, 10, 10, 20],    # False
    ]

    for bills in test_cases:
        print(f"Bills: {bills} -> Can give change: {solution.lemonadeChange(bills)}")
