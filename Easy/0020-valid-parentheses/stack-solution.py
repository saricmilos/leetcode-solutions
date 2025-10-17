from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if a string containing '()', '{}', and '[]' is valid.

        A string is valid if:
        1. Open brackets are closed by the same type of brackets.
        2. Open brackets are closed in the correct order.

        Args:
            s (str): The input string containing only '()', '{}', '[]'.

        Returns:
            bool: True if the string is valid, False otherwise.

        Time Complexity:
            O(n), where n is the length of the string. Each character is processed once.

        Space Complexity:
            O(n), in the worst case all characters are opening brackets and stored in the stack.
        """
        bracket_map = {")": "(", "}": "{", "]": "["}
        open_brackets = set(bracket_map.values())
        stack = []

        for char in s:
            if char in open_brackets:  # opening brackets
                stack.append(char)
            elif char in bracket_map:  # closing brackets
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # optional: invalid character
                return False

        return not stack  # True if stack is empty, else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))  
    print(sol.isValid("([)]"))    
    print(sol.isValid("{[]}"))    
