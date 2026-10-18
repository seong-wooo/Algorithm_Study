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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode root = new ListNode(0);
        root.next = head;
        ListNode node = root;
        
        Map<ListNode, ListNode> prevMap = new HashMap<>();
        
        while (node != null && node.next != null) {
            prevMap.put(node.next, node);
            node = node.next;
        }

        for (int i = 0; i < n; i++) {
            node = prevMap.get(node);
        }
        ListNode next = node.next.next;
        node.next.next = null;
        node.next = next;

        return root.next;
    }
}