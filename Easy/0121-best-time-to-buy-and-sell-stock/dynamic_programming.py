class Solution:
    """
    LeetCode 121 — Best Time to Buy and Sell Stock

    This class provides a method to determine the maximum profit achievable
    by buying and selling a single share of stock given a list of daily prices.

    The algorithm runs in O(n) time and O(1) space, making it efficient for
    large input arrays.

    Example:
        >>> solution = Solution()
        >>> prices = [7, 1, 5, 3, 6, 4]
        >>> solution.maxProfit(prices)
        5

        >>> prices = [7, 6, 4, 3, 1]
        >>> solution.maxProfit(prices)
        0
    """

    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculate the maximum profit from a single buy-sell transaction.

        Args:
            prices (list[int]): A list of integers representing the stock price on each day.

        Returns:
            int: The maximum profit possible. Returns 0 if no profit can be made.

        Example:
            >>> Solution().maxProfit([2, 4, 1])
            2
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


if __name__ == "__main__":
    # Example runs
    solution = Solution()
    print("Example 1:", solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
    print("Example 2:", solution.maxProfit([7, 6, 4, 3, 1]))    # Output: 0
