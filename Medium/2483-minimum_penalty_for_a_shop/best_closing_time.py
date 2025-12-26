"""
minimum_penalty.py

Module to find the optimal closing time for a shop to minimize penalties.

Example:
    >>> from minimum_penalty import Solution
    >>> sol = Solution()
    >>> sol.bestClosingTime("YYNY")
    2
"""

class Solution:
    """
    Solution to determine the best closing time for a shop to minimize penalties.

    Methods
    -------
    bestClosingTime(customers: str) -> int:
        Finds the hour to close the shop that results in the minimum penalty.
    """

    def bestClosingTime(self, customers: str) -> int:
        """
        Compute the earliest hour to close the shop to minimize penalties.

        Penalty rules:
        - +1 penalty if shop is open and no customer arrives ('N')
        - +1 penalty if shop is closed and a customer arrives ('Y')

        Parameters
        ----------
        customers : str
            A string representing customer arrivals each hour ('Y' or 'N').

        Returns
        -------
        int
            The earliest closing hour that minimizes the penalty.
        """
        # Start with the shop closed all day
        minimum_penalty = customers.count("Y")
        current_penalty = minimum_penalty
        best_closing_time = 0

        # Check each possible closing time
        for closing_time in range(1, len(customers) + 1):
            if customers[closing_time - 1] == "N":
                current_penalty += 1  # open and no customer
            else:
                current_penalty -= 1  # open and customer, penalty removed

            # Update best closing time if current penalty is lower
            if current_penalty < minimum_penalty:
                best_closing_time = closing_time

            # Keep track of minimum penalty
            minimum_penalty = min(current_penalty, minimum_penalty)

        return best_closing_time


if __name__ == "__main__":
    # Example usage
    sol = Solution()
    example_input = "YYNY"
    output = sol.bestClosingTime(example_input)
    print(f"Customer schedule: {example_input}")
    print(f"Best closing time: {output}")
