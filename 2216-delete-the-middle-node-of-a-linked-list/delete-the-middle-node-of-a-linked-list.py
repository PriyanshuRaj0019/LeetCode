from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If list contains only 1 node, deleting it yields an empty list
        if not head or not head.next:
            return None

        # Slow and fast pointers
        prev = None
        slow = head
        fast = head

        # Fast moves 2 steps, slow moves 1 step
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # 'slow' now points to the ⌊n / 2⌋-th node; skip it
        prev.next = slow.next

        return head