from typing import List


class Solution:
    """
    LeetCode 682 — Baseball Game

    Simulate the process of recording points in a baseball game.
    The input is a list of operations represented as strings:

        - An integer x : record a new score of x
        - "+"          : record a new score equal to the sum of the previous two valid scores
        - "D"          : record a new score equal to double the previous valid score
        - "C"          : invalidate the previous valid score, removing it from the record

    After all operations, return the total sum of the recorded scores.

    --------------------------------------------------------------------
    Time Complexity
    --------------------------------------------------------------------
    O(n)
        Each operation is processed exactly once, and each list operation
        (append, pop, index access) runs in constant time.

    --------------------------------------------------------------------
    Space Complexity
    --------------------------------------------------------------------
    O(n)
        In the worst case, all operations add new scores to the record,
        requiring space proportional to the number of operations.
    """

    def calPoints(self, operations: List[str]) -> int:
        """
        Calculate the final score after performing all operations.

        Parameters
        ----------
        operations : List[str]
            List of strings representing baseball game operations.

        Returns
        -------
        int
            The total score after applying all operations.

        Examples
        --------
        >>> Solution().calPoints(["5", "2", "C", "D", "+"])
        30
        >>> Solution().calPoints(["5","-2","4","C","D","9","+","+"])
        27
        """
        record: List[int] = []

        for op in operations:
            if op == "+":
                # Add sum of previous two valid scores
                record.append(record[-1] + record[-2])
            elif op == "D":
                # Add double of previous valid score
                record.append(2 * record[-1])
            elif op == "C":
                # Remove last valid score
                record.pop()
            else:
                # Add new score (integer value)
                record.append(int(op))

        return sum(record)


if __name__ == "__main__":
    examples = [
        ["5", "2", "C", "D", "+"],
        ["5", "-2", "4", "C", "D", "9", "+", "+"],
        ["1", "C"],
        ["10", "-5", "D", "+", "C"],
    ]

    solver = Solution()
    for ops in examples:
        print(f"Operations: {ops}")
        print(f"Total score: {solver.calPoints(ops)}")
        print("-" * 40)
