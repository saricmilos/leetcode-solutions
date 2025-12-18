from typing import List

class Solution:
    """
    Solution for LeetCode 905: Sort Array By Parity.
    
    Moves all even numbers to the front and odd numbers to the back.
    The relative order of numbers within even/odd groups does not matter.
    """

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        first_i, last_i = 0, len(nums) - 1
        
        while first_i < last_i:
            if nums[first_i] % 2 > nums[last_i] % 2:
                # Swap odd at first_i with even at last_i
                nums[first_i], nums[last_i] = nums[last_i], nums[first_i]
            
            if nums[first_i] % 2 == 0:
                first_i += 1
            if nums[last_i] % 2 == 1:
                last_i -= 1
        
        return nums


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [3, 1, 2, 4],
        [0, 1, 2],
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        []
    ]
    
    for nums in test_cases:
        print(f"Input: {nums} -> Sorted by parity: {solution.sortArrayByParity(nums)}")
