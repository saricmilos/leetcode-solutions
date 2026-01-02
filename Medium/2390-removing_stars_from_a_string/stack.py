class Solution:
    def removeStars(self, s: str) -> str:
        """
        Remove stars from a string.

        Each '*' removes itself and the closest non-star character to its left.

        :param s: Input string containing letters and '*'
        :return: Resulting string after all removals
        """
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
