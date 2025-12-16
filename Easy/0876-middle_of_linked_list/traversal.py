from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Returns the middle node of a singly-linked list.
        If there are two middle nodes, returns the second one.

        Args:
            head (Optional[ListNode]): Head of the linked list.

        Returns:
            Optional[ListNode]: Middle node of the list.
        """
        # First pass: count the total number of nodes
        total_nodes = 0
        traversal = head
        while traversal:
            total_nodes += 1
            traversal = traversal.next

        # Second pass: move to the middle node
        steps_to_middle = total_nodes // 2
        middle = head
        for _ in range(steps_to_middle):
            middle = middle.next

        return middle


# ------------------- Runnable Example -------------------
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    nodes = [ListNode(i) for i in range(1, 7)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    solution = Solution()
    middle = solution.middleNode(nodes[0])
    print(f"Middle node value: {middle.val}")  # Should print 4
