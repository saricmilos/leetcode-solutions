from typing import List

class Solution:
    """
    In-place algorithm to move all 0's in an integer list to the end while preserving
    the relative order of the non-zero elements.

    This implementation follows the two-pointer / fast-slow approach:
    - `write_idx` (slow pointer) tracks the position where the next non-zero
      element should be placed.
    - Iterate over the list with `read_num` and copy non-zero values to `write_idx`,
      incrementing `write_idx` each time.
    - After the loop, fill the remaining positions with 0.

    This method mutates the input list `nums` and returns None (LeetCode-style).
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeros in `nums` to the end in-place.

        Args:
            nums: List[int] -- list of integers to reorder in-place.

        Returns:
            None -- `nums` is modified in-place.

        Examples:
            >>> arr = [0, 1, 0, 3, 12]
            >>> Solution().moveZeroes(arr)
            >>> arr
            [1, 3, 12, 0, 0]

            >>> arr = [0, 0, 0]
            >>> Solution().moveZeroes(arr)
            >>> arr
            [0, 0, 0]

            >>> arr = [1, 2, 3]
            >>> Solution().moveZeroes(arr)
            >>> arr
            [1, 2, 3]
        """
        write_idx = 0  # position to write the next non-zero element

        # 1) Move non-zero elements forward, preserving order.
        for num in nums:
            if num != 0:
                nums[write_idx] = num
                write_idx += 1

        # 2) Fill remaining positions with zeros.
        if write_idx < len(nums):  # only do work if there are zeros to append
            nums[write_idx:] = [0] * (len(nums) - write_idx)

if __name__ == "__main__":
    examples = [
        [0, 1, 0, 3, 12],
        [0, 0, 0],
        [1, 2, 3],
        []
    ]

    sol = Solution()
    for arr in examples:
        original = arr.copy()
        sol.moveZeroes(arr)
        print(f"before: {original} -> after: {arr}")

    # Quick assertions (unit-test style)
    a = [0, 1, 0, 3, 12]
    sol.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]

    b = [0, 0, 0]
    sol.moveZeroes(b)
    assert b == [0, 0, 0]

    c = [1, 2, 3]
    sol.moveZeroes(c)
    assert c == [1, 2, 3]

    print("All example assertions passed.")
