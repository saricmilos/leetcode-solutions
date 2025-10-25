from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Readable string representation for debugging."""
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"


class Solution:
    def reverseList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        """
        Reverse a singly linked list in-place.

        This method iteratively reverses the pointers of each node in a linked list.
        By maintaining references to the current node, previous node, and next node,
        we can reverse the direction of the list efficiently in a single pass.

        Args:
            head (ListNode | None): The head of the linked list.

        Returns:
            ListNode | None: The new head of the reversed linked list.

        Example:
            >>> # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
            >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            >>> Solution().reverseList(head)
            5 -> 4 -> 3 -> 2 -> 1

        Time Complexity:
            O(n) — Each node is visited exactly once.

        Space Complexity:
            O(1) — Reversal is done in place using a few pointers.
        """
        previous = None
        current = head

        while current:
            next_node = current.next      # Save next node
            current.next = previous       # Reverse the pointer
            previous = current            # Move previous one step forward
            current = next_node           # Move current one step forward

        return previous  # 'previous' becomes the new head after the loop


# Example usage
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original list:")
    print(head)

    print("\nReversed list:")
    new_head = Solution().reverseList(head)
    print(new_head)
