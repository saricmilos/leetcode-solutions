from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        """
        Finds a pair of candy sizes (one from Alice, one from Bob) to swap
        so that both end up with the same total candy amount.

        Args:
            aliceSizes (List[int]): List of Alice's candy sizes.
            bobSizes (List[int]): List of Bob's candy sizes.

        Returns:
            List[int]: The candy sizes to swap [alice_candy, bob_candy].
        """
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)
        alice_set = set(aliceSizes)

        for candy_bob in bobSizes:
            candy_alice = (total_alice - total_bob + 2 * candy_bob) // 2
            if candy_alice in alice_set:
                return [candy_alice, candy_bob]


# ------------------- Runnable Example -------------------
if __name__ == "__main__":
    solution = Solution()
    alice = [1,2,5]
    bob = [2,4]
    print(solution.fairCandySwap(alice, bob))  # Output: [5,4]
