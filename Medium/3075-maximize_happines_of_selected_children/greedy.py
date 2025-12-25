from typing import List

class Solution:
    """
    Solution to maximize the happiness of selected children.

    The goal is to select up to k children such that the sum of their happiness 
    is maximized. The happiness of each selected child decreases by the number 
    of children picked before them (cannot go below zero).

    Methods
    -------
    maximumHappinessSum(happiness: List[int], k: int) -> int
        Calculates the maximum possible happiness sum for k selected children.
    """

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        Calculate the maximum happiness sum by selecting up to k children.

        Parameters
        ----------
        happiness : List[int]
            List of happiness values for each child.
        k : int
            Maximum number of children to select.

        Returns
        -------
        int
            Maximum sum of happiness after selecting k children.
        
        Example
        -------
        >>> sol = Solution()
        >>> sol.maximumHappinessSum([5, 3, 2, 4], 3)
        11
        >>> sol.maximumHappinessSum([1, 1, 1], 2)
        2
        """
        # Sort the happiness array in descending order to prioritize the happiest children
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        # Iterate through the first k children (highest happiness)
        for turn_index, happiness_value in enumerate(happiness[:k]):
            # Adjust happiness: decreases by the number of children picked before
            adjusted_happiness = happiness_value - turn_index
            total_happiness += max(adjusted_happiness, 0)  # Avoid negative happiness
        
        return total_happiness


# ------------------- Runnable Examples -------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    happiness_list = [5, 3, 2, 4]
    k = 3
    print(f"Maximum happiness for {k} children: {sol.maximumHappinessSum(happiness_list, k)}")
    # Output: 11

    # Example 2
    happiness_list = [1, 1, 1]
    k = 2
    print(f"Maximum happiness for {k} children: {sol.maximumHappinessSum(happiness_list, k)}")
    # Output: 2

    # Example 3
    happiness_list = [10, 8, 5, 3]
    k = 4
    print(f"Maximum happiness for {k} children: {sol.maximumHappinessSum(happiness_list, k)}")
    # Output: 22
