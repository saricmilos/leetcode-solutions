# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        LeetCode 2. Add Two Numbers
        -------------------------------------
        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each node contains a single digit.
        Add the two numbers and return the sum as a linked list.

        The function performs digit-by-digit addition, keeping track of carry,
        and builds a new linked list to represent the result.
        """

        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        # Traverse both lists until all digits and carry are processed
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            # Create a new node with the resulting digit
            current.next = ListNode(total % 10)
            current = current.next

            # Advance the input list pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
