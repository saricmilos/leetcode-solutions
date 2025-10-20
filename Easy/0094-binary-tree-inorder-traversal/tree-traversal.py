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
    Solution for inorder traversal of a binary tree (LeetCode 94).
    
    Inorder traversal visits nodes in the order: left subtree -> current node -> right subtree.
    This implementation uses recursion.
    
    Time Complexity: O(n), where n is the number of nodes
    Space Complexity: O(h), recursion stack, h = height of the tree
    """

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform inorder traversal of a binary tree.

        Args:
            root (Optional[TreeNode]): Root node of the binary tree.

        Returns:
            List[int]: List of node values in inorder sequence.
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


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
