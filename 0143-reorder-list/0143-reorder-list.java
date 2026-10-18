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
    public void reorderList(ListNode head) {
        // fast, slow 로 중간 지점을 찾는다.
        //  중간 ~ 끝 뒤집는다.
        // merge한다. 

        ListNode root = new ListNode(0, head);

        ListNode fast = root;
        ListNode slow = root;

        // slow 까지가 유지
        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        ListNode cur = slow.next;
        slow.next = null;
        ListNode prev = null;

        while(cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        ListNode left = root.next;
        ListNode right = prev;

        while(left != null) {
            ListNode leftNext = left.next;
            if (right == null) {
                break;
            }
            ListNode rightNext = right.next;
            
            left.next = right;
            right.next = leftNext;
            left = right.next;
            right = rightNext;
        }
    }
}