"""
Insert Greatest Common Divisors in a Linked List
------------------------------------------------

For every adjacent pair of nodes in a singly linked list,
insert a new node whose value is the greatest common divisor (GCD)
of the two adjacent node values.

This implementation follows the Euclidean algorithm for GCD
and modifies the list in-place.

Author: Your Name
"""

from typing import Optional, List


class ListNode:
    """
    Definition for a singly-linked list node.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    """
    Solution class containing the logic to insert GCD nodes.
    """

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Inserts a node containing the GCD between every adjacent
        pair of nodes in the linked list.

        Args:
            head (Optional[ListNode]): Head of the singly linked list

        Returns:
            Optional[ListNode]: Head of the modified linked list
        """

        def gcd(a: int, b: int) -> int:
            """
            Compute the greatest common divisor using
            the Euclidean algorithm.
            """
            while b != 0:
                a, b = b, a % b
            return a

        current = head

        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)

            gcd_node = ListNode(gcd_value, current.next)
            current.next = gcd_node

            current = gcd_node.next

        return head


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Build a linked list from a Python list.

    Args:
        values (List[int]): List of integer values

    Returns:
        Optional[ListNode]: Head of the linked list
    """
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert a linked list to a Python list.

    Args:
        head (Optional[ListNode]): Head of the linked list

    Returns:
        List[int]: List of node values
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def main():
    """
    Runnable example demonstrating the solution.
    """
    values = [18, 6, 10]
    print("Original list:", values)

    head = build_linked_list(values)
    solution = Solution()
    modified_head = solution.insertGreatestCommonDivisors(head)

    print("Modified list:", linked_list_to_list(modified_head))


if __name__ == "__main__":
    main()
