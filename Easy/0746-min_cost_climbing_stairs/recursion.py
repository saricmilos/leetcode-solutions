from typing import List

class Solution:
    """
    Solution for the Min Cost Climbing Stairs problem.

    Problem:
        Given an array `cost` where `cost[i]` is the cost of step i,
        you can climb 1 or 2 steps at a time. Return the minimum cost
        to reach the top of the staircase.

    Approach:
        This solution uses memoized recursion (top-down dynamic programming).
        - min_cost[n] stores the minimum cost to reach step n.
        - Base cases: 0 and 1 steps cost 0 to reach.
        - Recursive relation:
            min_cost[step] = min(
                min_cost[step-1] + cost[step-1],
                min_cost[step-2] + cost[step-2]
            )
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = {0: 0, 1: 0}
        n_steps = len(cost)

        def find_min_cost(step: int) -> int:
            if step in min_cost:
                return min_cost[step]
            # Recurrence: min cost to reach this step
            min_cost[step] = min(
                find_min_cost(step - 1) + cost[step - 1],
                find_min_cost(step - 2) + cost[step - 2]
            )
            return min_cost[step]

        return find_min_cost(n_steps)


if __name__ == "__main__":
    # Example usage
    example_costs = [
        [10, 15, 20],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ]

    solution = Solution()
    for i, cost in enumerate(example_costs, 1):
        result = solution.minCostClimbingStairs(cost)
        print(f"Example {i}: cost = {cost} -> minimum cost to reach top = {result}")
