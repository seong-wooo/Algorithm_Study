/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode half = null, slow = head, fast = head;

        while(fast != null && fast.next != null) {
            half = slow;
            fast = fast.next.next;
            slow = slow.next;
        }

        half.next = null;

        ListNode n1 = sortList(head);
        ListNode n2 = sortList(slow);
        return merge(n1, n2);
    }

    public ListNode merge(ListNode n1, ListNode n2) {
        if (n1 == null) {
            return n2;
        }
        if (n2 == null) {
            return n1;
        }

        if (n1.val < n2.val) {
            n1.next = merge(n1.next, n2);
            return n1;
        } 
        
        n2.next = merge(n1, n2.next);
        return n2;
    }
}