"""
laser_beams.py

Module to calculate the number of laser beams in a bank based on security device placement.

Example:
    >>> from laser_beams import Solution
    >>> sol = Solution()
    >>> sol.numberOfBeams(["011001", "000000", "010100", "001000"])
    8
"""

from typing import List

class Solution:
    """
    Solution to compute the number of laser beams in a bank.

    Methods
    -------
    numberOfBeams(bank: List[str]) -> int:
        Calculates total laser beams formed between security devices.
    """

    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Compute the number of laser beams in a bank.

        A laser beam exists between two rows if:
        - Both rows have at least one device ('1')
        - All rows in between are empty (contain only '0')

        The number of beams between two consecutive non-empty rows
        is the product of the number of devices in each row.

        Parameters
        ----------
        bank : List[str]
            List of strings representing the bank layout ('0' or '1') per row.

        Returns
        -------
        int
            Total number of laser beams in the bank.
        """
        laser_beams = 0

        # Keep only rows that contain at least one device
        filtered_bank = [row for row in bank if '1' in row]

        # Count beams between consecutive non-empty rows
        for i in range(len(filtered_bank) - 1):
            laser_beams += filtered_bank[i].count('1') * filtered_bank[i + 1].count('1')

        return laser_beams


if __name__ == "__main__":
    # Example usage
    sol = Solution()
    example_input = ["011001", "000000", "010100", "001000"]
    output = sol.numberOfBeams(example_input)
    print(f"Bank layout: {example_input}")
    print(f"Total laser beams: {output}")
