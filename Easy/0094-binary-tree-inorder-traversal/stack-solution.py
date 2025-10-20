from typing import List, Optional

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Iterative solution for inorder traversal of a binary tree using a stack.

    Inorder traversal visits nodes in the order: left subtree -> current node -> right subtree.

    Benefits of the iterative stack-based approach:
        1. Avoids recursion depth limits: Handles very deep trees without risk of RecursionError.
        2. Explicit control of traversal: The stack is user-controlled, enabling early exit or extra processing.
        3. More efficient for large trees: Avoids function call overhead of recursion.
        4. Flexible for advanced variants: Can be adapted for Morris traversal or threaded trees.
        5. Consistent across languages: Works safely in languages with small call stacks.
    
    Time Complexity: O(n), where n is the number of nodes
    Space Complexity: O(h), where h is the height of the tree (stack usage)
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform inorder traversal of a binary tree iteratively using a stack.

        Args:
            root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
            List[int]: List of node values in inorder sequence.
        """
        result = []
        stack = []
        current = root

        # Traverse until there are no nodes left to process
        while current or stack:
            # Reach the leftmost node
            while current:
                stack.append(current)
                current = current.left
            # Process the node
            current = stack.pop()
            result.append(current.val)
            # Visit the right subtree
            current = current.right

        return result


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    # Example tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    sol = Solution()
    result = sol.inorderTraversal(root)
    print(result)  # Output: [4, 2, 5, 1, 3]
