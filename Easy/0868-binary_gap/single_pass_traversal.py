class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Returns the maximum distance between two consecutive '1's
        in the binary representation of the given integer.
        """
        binary_str = bin(n)[2:]
        previous_index = None
        max_gap = 0

        for index, bit in enumerate(binary_str):
            if bit == '1':
                if previous_index is not None:
                    max_gap = max(max_gap, index - previous_index)
                previous_index = index

        return max_gap


# ------------------- Runnable Examples -------------------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        22,   # binary: 10110 → gap = 2
        8,    # binary: 1000  → gap = 0
        5,    # binary: 101   → gap = 2
        6,    # binary: 110   → gap = 1
        1     # binary: 1     → gap = 0
    ]

    for n in test_cases:
        print(f"n = {n}, binary = {bin(n)[2:]}, binary gap = {solution.binaryGap(n)}")
