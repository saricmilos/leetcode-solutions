from typing import Optional, List, Tuple

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
    Iterative solution for LeetCode 100: Same Tree using a stack.

    This approach compares two binary trees iteratively using a stack.
    Nodes from both trees are processed in pairs (node from tree1, node from tree2).

    Benefits:
        1. Avoids recursion depth limits (safe for very deep trees).
        2. Explicit control over traversal with a stack.
        3. Efficient: O(n) time, O(h) space (h = height of the tree).
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are identical iteratively.

        Args:
            p (Optional[TreeNode]): Root of the first tree.
            q (Optional[TreeNode]): Root of the second tree.

        Returns:
            bool: True if the trees are structurally identical and have the same node values, False otherwise.
        """
        stack: List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            # Both nodes are None → identical at this position
            if not node1 and not node2:
                continue
            # One node is None → trees differ
            if not node1 or not node2:
                return False
            # Node values differ
            if node1.val != node2.val:
                return False

            # Push right and left children as pairs
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True


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
