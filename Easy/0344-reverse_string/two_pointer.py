from typing import List

class Solution:
    """
    Reverse a list of characters in-place.

    Problem statement:
        Given a list of characters `s`, reverse it in-place without returning anything.

    Time complexity: O(n), where n = len(s)
    Space complexity: O(1), in-place
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Reverse the list `s` in-place.

        Args:
            s: List[str] -- list of characters to reverse

        Returns:
            None -- modifies `s` in-place

        Examples:
            >>> arr = ["h","e","l","l","o"]
            >>> Solution().reverseString(arr)
            >>> arr
            ['o','l','l','e','h']

            >>> arr = ["H","a","n","n","a","h"]
            >>> Solution().reverseString(arr)
            >>> arr
            ['h','a','n','n','a','H']
        """
        n = len(s)
        for i in range(n // 2):
            # Swap the i-th element with the mirrored element
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


if __name__ == "__main__":
    sol = Solution()
    examples = [
        ["h","e","l","l","o"],
        ["H","a","n","n","a","h"],
        [],
        ["a"]
    ]

    for arr in examples:
        original = arr.copy()
        sol.reverseString(arr)
        print(f"before: {original} -> after: {arr}")
