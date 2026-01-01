class Solution:
    def maxOperations(self, nums, k):
        """
        Returns the maximum number of operations where each operation consists
        of removing two numbers from the array whose sum equals k.

        Approach:
        - Sort the array.
        - Use two pointers: one starting at the beginning (left) and one at the end (right).
        - Compare the sum of values at both pointers and adjust pointers accordingly.
        - Count valid pairs while ensuring each element is used at most once.

        Time Complexity:
        - O(n log n), due to sorting.

        Space Complexity:
        - O(1) extra space (excluding sorting overhead).
        """

        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return operations
