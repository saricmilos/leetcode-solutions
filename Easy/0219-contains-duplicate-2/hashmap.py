"""

Given an integer array `nums` and an integer `k`, return True if there are
two distinct indices i and j in the array such that:
    - nums[i] == nums[j], and
    - abs(i - j) <= k

Example:
    Input: nums = [1, 2, 3, 1], k = 3
    Output: True
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Checks whether the list `nums` contains two identical numbers
        whose indices differ by at most `k`.

        Algorithm:
            - Use a hash map to store the last seen index of each number.
            - For each element, check if the number was seen before and
              whether the distance between indices is ≤ k.
            - Return True if such a pair exists, otherwise False.

        Time Complexity:
            O(n) — each element is processed once.

        Space Complexity:
            O(n) — dictionary may store up to n unique elements.

        Args:
            nums (List[int]): List of integers.
            k (int): Maximum allowed index distance.

        Returns:
            bool: True if a duplicate exists within distance k, else False.
        """
        seen_indices = {}

        for i, number in enumerate(nums):
            if number in seen_indices and i - seen_indices[number] <= k:
                return True
            seen_indices[number] = i

        return False


def main():
    """Run example test cases."""
    solution = Solution()

    # Example 1
    nums1, k1 = [1, 2, 3, 1], 3
    print(f"Input: nums={nums1}, k={k1} -> Output: {solution.containsNearbyDuplicate(nums1, k1)}")

    # Example 2
    nums2, k2 = [1, 0, 1, 1], 1
    print(f"Input: nums={nums2}, k={k2} -> Output: {solution.containsNearbyDuplicate(nums2, k2)}")

    # Example 3
    nums3, k3 = [1, 2, 3, 4], 2
    print(f"Input: nums={nums3}, k={k3} -> Output: {solution.containsNearbyDuplicate(nums3, k3)}")

    # Example 4
    nums4, k4 = [99, 99], 2
    print(f"Input: nums={nums4}, k={k4} -> Output: {solution.containsNearbyDuplicate(nums4, k4)}")

    # Example 5
    nums5, k5 = [1, 2, 3, 1, 2, 3], 2
    print(f"Input: nums={nums5}, k={k5} -> Output: {solution.containsNearbyDuplicate(nums5, k5)}")


if __name__ == "__main__":
    main()
