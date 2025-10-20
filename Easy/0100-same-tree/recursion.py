from typing import Optional

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
    Solution for LeetCode 100: Same Tree

    Determines if two binary trees are structurally identical and have the same node values.

    Approach:
        - Recursively compare corresponding nodes in both trees.
        - Base cases:
            1. If both nodes are None → trees are identical at this position.
            2. If one node is None and the other is not → trees differ.
            3. If node values differ → trees differ.
        - Recursively check left and right subtrees.
    
    Time Complexity: O(n), where n is the number of nodes (both trees)
    Space Complexity: O(h), recursion stack, h = height of the tree
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are the same.

        Args:
            p (Optional[TreeNode]): Root of the first binary tree.
            q (Optional[TreeNode]): Root of the second binary tree.

        Returns:
            bool: True if the trees are identical, False otherwise.
        """
        # Both nodes are None → identical at this position
        if not p and not q:
            return True
        # One node is None → trees differ
        if not p or not q:
            return False
        # Current node values must match and recurse on left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    # Tree 1
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    # Tree 2 (identical to tree1)
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    # Tree 3 (different)
    tree3 = TreeNode(1, TreeNode(2))

    sol = Solution()
    print(sol.isSameTree(tree1, tree2))  # Output: True
    print(sol.isSameTree(tree1, tree3))  # Output: False
