class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb a staircase of `n` steps,
        where each move allows climbing either 1 step or 2 steps.

        This is a classic dynamic programming problem, often referred to as 
        the "Climbing Stairs" problem. The problem can be reduced to computing
        the `n`-th Fibonacci number, where:
        
        - f(1) = 1  (1 way to climb 1 step)
        - f(2) = 2  (2 ways: (1+1) or (2))
        - f(n) = f(n-1) + f(n-2) for n > 2

        Parameters
        ----------
        n : int
            The total number of steps in the staircase. Must be a positive integer.

        Returns
        -------
        int
            The total number of distinct ways to climb to the top.

        Complexity Analysis
        -------------------
        Time Complexity: O(n)
            - The algorithm iterates once from step 3 to step n, performing O(1) work at each iteration.
            - Hence, the runtime grows linearly with respect to `n`.

        Space Complexity: O(1)
            - Only two variables (`a` and `b`) are used to store the last two computed results.
            - No additional data structures proportional to `n` are used.
            - Therefore, the memory usage is constant.
        """
        if n <= 2:
            return n

        a, b = 1, 2  # base cases for f(1) and f(2)
        for _ in range(3, n + 1):
            a, b = b, a + b  # update to next Fibonacci number
        return b


if __name__ == "__main__":
    # Example usage and simple test cases
    sol = Solution()

    print("climbStairs(2) =", sol.climbStairs(2))  # Expected: 2
    print("climbStairs(3) =", sol.climbStairs(3))  # Expected: 3
    print("climbStairs(5) =", sol.climbStairs(5))  # Expected: 8
    print("climbStairs(10) =", sol.climbStairs(10))  # Expected: 89
