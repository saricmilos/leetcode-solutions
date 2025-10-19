"""
LeetCode 83 — Remove Duplicates from Sorted List.

This module provides:
- A simple `ListNode` singly-linked list implementation used by LeetCode-style problems.
- `Solution.deleteDuplicates` which removes duplicates from a sorted singly-linked list
  (keeps one copy of each value).
- Helper functions for building and converting linked lists for easy testing and demonstration.
- Runnable examples and basic assertions in the `__main__` block.

"""

from __future__ import annotations
from typing import Optional, List


class ListNode:
    """Singly-linked list node.

    Attributes:
        val: The integer value stored in the node.
        next: Reference to the next ListNode or None.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        """Compact representation showing the value (useful in debugging)."""
        return f"ListNode({self.val})"


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Build a singly-linked list from a list of integers.

    Args:
        values: Sequence of integers in order.

    Returns:
        The head ListNode of the constructed linked list or None for empty input.
    """
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert a singly-linked list to a Python list of integers.

    Args:
        head: Head of the linked list.

    Returns:
        List of integer values in order.
    """
    out: List[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


class Solution:
    """
    Solution container for remove-duplicates function.

    Methods:
        deleteDuplicates(head): Remove duplicates from a sorted linked list in-place.
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicates from a sorted singly-linked list such that each element
        appears only once. The operation is done in-place.

        Time complexity: O(n), where n is the number of nodes.
        Space complexity: O(1) extra space (in-place).

        Args:
            head: Head of the sorted linked list.

        Returns:
            Head of the modified list with duplicates removed (keeping one copy).
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate node by pointing around it.
                current.next = current.next.next
            else:
                # Only advance when next node has a different value.
                current = current.next
        return head


if __name__ == "__main__":
    # Runnable examples + simple assertions for quick sanity checks.

    solution = Solution()

    examples = [
        # (input list, expected output list)
        ([], []),
        ([1], [1]),
        ([1, 1], [1]),
        ([1, 1, 1], [1]),
        ([1, 1, 2], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([0, 0, 1, 1, 1, 2, 3, 3], [0, 1, 2, 3]),
        # large block of duplicates
        ([5] * 10 + [6, 6, 7], [5, 6, 7]),
    ]

    for inp, expected in examples:
        head = build_linked_list(inp)
        new_head = solution.deleteDuplicates(head)
        out = to_list(new_head)
        print(f"input: {inp} -> output: {out}  (expected: {expected})")
        assert out == expected, f"Test failed: input {inp} produced {out}, expected {expected}"

    print("All tests passed.")
