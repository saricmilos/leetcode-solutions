from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return a new sorted linked list.

        Args:
            list1 (Optional[ListNode]): First sorted linked list.
            list2 (Optional[ListNode]): Second sorted linked list.

        Returns:
            Optional[ListNode]: Head of the merged sorted linked list.

        Time Complexity:
            O(n + m), where n and m are the lengths of list1 and list2. Each node is processed once.

        Space Complexity:
            O(1), only pointers are used; no extra data structures are created.
        """
        dummy = ListNode()  # Dummy node to simplify edge cases
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    sol = Solution()
    merged = sol.mergeTwoLists(l1, l2)

    # Print merged list
    while merged:
        print(merged.val, end=" -> " if merged.next else "")
        merged = merged.next
