from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        """
        Generate a permutation of [0, 1, ..., len(s)] that satisfies the DI string pattern.

        Parameters
        ----------
        s : str
            A string consisting of 'I' (increase) and 'D' (decrease).

        Returns
        -------
        List[int]
            A list of integers [0, 1, ..., len(s)] forming a valid permutation
            that satisfies the DI pattern.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        low, high = 0, len(s)
        result = []

        for char in s:
            if char == "I":
                result.append(low)
                low += 1
            else:  # 'D'
                result.append(high)
                high -= 1

        # Append the last remaining number
        result.append(low)  # low == high here
        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("IDID", [0,4,1,3,2]),
        ("III", [0,1,2,3]),
        ("DDI", [3,2,0,1]),
        ("", [0]),  # Edge case, empty string
    ]

    for s, expected in test_cases:
        result = solution.diStringMatch(s)
        print(f"Input: '{s}' | Output: {result} | Expected pattern: {expected}")
