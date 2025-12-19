class Solution:
    def validMountainArray(self, arr):
        """
        Determine whether an array is a valid mountain array.

        A valid mountain array must:
        - Have at least 3 elements
        - Strictly increase to a single peak
        - Strictly decrease after the peak
        - The peak cannot be the first or last element

        Parameters
        ----------
        arr : List[int]
            The input array of integers.

        Returns
        -------
        bool
            True if arr is a valid mountain array, False otherwise.

        Time Complexity
        ---------------
        O(n), where n is the length of the array.

        Space Complexity
        ----------------
        O(1), constant extra space.
        """

        if len(arr) < 3:
            return False

        peak_i = 0

        # Step 1: Walk up (strictly increasing)
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                peak_i += 1
            else:
                break

        # Peak cannot be first or last element
        if peak_i == 0 or peak_i == len(arr) - 1:
            return False

        counter = peak_i

        # Step 2: Walk down (strictly decreasing)
        for i in range(peak_i, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                counter += 1
            else:
                break

        # All steps must be valid
        return counter == len(arr) - 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 1], False),                 # Too short
        ([3, 5, 5], False),              # Flat at peak
        ([0, 3, 2, 1], True),             # Valid mountain
        ([0, 2, 3, 3, 5, 2, 1], False),   # Plateau
        ([0, 1, 2, 3, 4, 5], False),      # Only increasing
        ([5, 4, 3, 2, 1], False),         # Only decreasing
        ([1, 3, 2], True),                # Small valid mountain
    ]

    for arr, expected in test_cases:
        result = solution.validMountainArray(arr)
        print(f"Input: {arr} | Output: {result} | Expected: {expected}")
