from typing import List


class Solution:
    """
    Solve the Longest Continuous Increasing Subsequence (LCIS) problem.

    The method implemented here computes the length of the longest strictly increasing
    contiguous subsequence in a one-dimensional list of integers.

    Methods
    -------
    find_length_of_lcis(nums: List[int]) -> int
        Return the length of the longest strictly increasing contiguous subsequence.

    Complexity
    ----------
    Time complexity: O(n)
        We perform a single pass over the input list `nums`, comparing adjacent elements
        and maintaining two counters (`current` and `longest`). Thus the runtime grows
        linearly with the input size `n = len(nums)`.

    Space complexity: O(1)
        Only a fixed number of integer variables are used regardless of input size.
        No extra data structures are allocated that scale with `n`.
    """

    def find_length_of_lcis(self, nums: List[int]) -> int:
        """
        Return the length of the longest strictly increasing contiguous subsequence.

        Parameters
        ----------
        nums : List[int]
            The input list of integers (may be empty).

        Returns
        -------
        int
            The length of the longest strictly increasing contiguous subsequence.

        Examples
        --------
        >>> Solution().find_length_of_lcis([])
        0

        >>> Solution().find_length_of_lcis([1])
        1

        >>> Solution().find_length_of_lcis([1,3,5,4,7])
        3

        >>> Solution().find_length_of_lcis([2,2,2])
        1

        >>> Solution().find_length_of_lcis([1,2,3,4,5])
        5
        """
        if not nums:
            return 0

        longest = 1
        current = 1

        # Iterate from the second element to the end
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # strictly increasing: extend the current run
                current += 1
            else:
                # run ended; update longest if needed and reset current
                if current > longest:
                    longest = current
                current = 1

        # In case the longest run continues until the end of the list
        return max(longest, current)


def _run_examples() -> None:
    """Run a small set of examples and print results.

    This helper is executed when running the module as a script and provides
    human-readable outputs for quick verification.
    """
    examples = [
        [],
        [1],
        [1, 3, 5, 4, 7],
        [2, 2, 2],
        [1, 2, 3, 4, 5],
        [1, 3, 2, 4, 6, 5, 7, 8],
    ]

    solver = Solution()
    print("Longest Continuous Increasing Subsequence — Examples")
    print("""------------------------------------------------
""")
    for arr in examples:
        length = solver.find_length_of_lcis(arr)
        print(f"nums = {arr}\nLCIS length = {length}\n")


if __name__ == "__main__":
    _run_examples()
