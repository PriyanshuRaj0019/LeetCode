
class Solution:
    def pairSum(self, head):
        slow = fast = head
        prev = None

        # Find the middle and reverse the first half
        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Calculate maximum twin sum
        maximum = 0

        while slow:
            maximum = max(maximum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return maximum
