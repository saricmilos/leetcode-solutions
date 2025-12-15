"""
Flipping an Image (LeetCode 832)

This module provides a solution to flip a binary image horizontally
and then invert it.

Technique Used:
- Array slicing for horizontal flipping
- List comprehension for binary inversion

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


class Solution:
    def flipAndInvertImage(self, image):
        """
        Flips the image horizontally and then inverts it.

        :param image: List[List[int]] - Binary matrix
        :return: List[List[int]] - Flipped and inverted matrix
        """
        inverted_image = []

        for row in image:
            # Step 1: Flip the row horizontally
            flipped = row[::-1]

            # Step 2: Invert the flipped row
            inverted = [1 if x == 0 else 0 for x in flipped]

            inverted_image.append(inverted)

        return inverted_image


if __name__ == "__main__":
    # Runnable example
    image = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]

    solution = Solution()
    result = solution.flipAndInvertImage(image)

    print("Input Image:")
    for row in image:
        print(row)

    print("\nFlipped and Inverted Image:")
    for row in result:
        print(row)
