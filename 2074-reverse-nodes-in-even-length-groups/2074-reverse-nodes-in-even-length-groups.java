/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseEvenLengthGroups(ListNode head) {
        // 'prevGroupEnd' keeps track of the node just before the current group
        ListNode prevGroupEnd = head; 
        int groupLen = 2; // Head is group 1 (length 1, always odd), so start at group 2
        
        while (prevGroupEnd.next != null) {
            ListNode curr = prevGroupEnd.next;
            int actualLen = 0;
            
            // 1. Count actual nodes available for the current group
            ListNode runner = curr;
            while (runner != null && actualLen < groupLen) {
                runner = runner.next;
                actualLen++;
            }
            
            // 2. If the actual length is even, reverse the group
            if (actualLen % 2 == 0) {
                ListNode prev = runner; // Connect the tail of reversed group to the next group's head
                ListNode nextNode = null;
                
                // Classic standard linked list reversal for 'actualLen' nodes
                for (int i = 0; i < actualLen; i++) {
                    nextNode = curr.next;
                    curr.next = prev;
                    prev = curr;
                    curr = nextNode;
                }
                
                // Connect the previous group's end to the new head of this reversed group
                ListNode temp = prevGroupEnd.next;
                prevGroupEnd.next = prev;
                prevGroupEnd = temp; // The old head is now the new tail of this group
            } else {
                // 3. If odd, just skip the group without reversing
                for (int i = 0; i < actualLen; i++) {
                    prevGroupEnd = prevGroupEnd.next;
                }
            }
            
            // Increment expected group length for the next iteration
            groupLen++;
        }
        
        return head;
    }
}