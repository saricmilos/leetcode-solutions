# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Readable string representation for debugging."""
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Remove all elements from a linked list that have a given value.

        This function traverses the linked list once, removing nodes whose value equals `val`.
        A dummy node is used to simplify edge cases, such as when the head node needs to be removed.

        Args:
            head (ListNode): The head of the singly linked list.
            val (int): The value to remove from the list.

        Returns:
            ListNode: The head of the modified linked list.

        Example:
            >>> # Create linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
            >>> head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
            >>> Solution().removeElements(head, 6)
            1 -> 2 -> 3 -> 4 -> 5

        Time Complexity:
            O(n) — The algorithm traverses the linked list once, where n is the number of nodes.

        Space Complexity:
            O(1) — Only a few extra pointers (`dummy`, `current`) are used regardless of input size.
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


# Example usage:
if __name__ == "__main__":
    # Build linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

    print("Original list:")
    print(head)

    print("\nAfter removing elements with value 6:")
    new_head = Solution().removeElements(head, 6)
    print(new_head)
