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
    public ListNode mergeKLists(ListNode[] lists) {
        Queue<ListNode> pq = new PriorityQueue<>((a,b) -> a.val - b.val);

        for (ListNode node: lists) {
            while (node != null) {
                pq.add(node);
                node = node.next;
            }
        }
        if (pq.isEmpty()) {
            return null;
        }

        ListNode head = pq.poll();
        ListNode root = head;

        while(!pq.isEmpty()) {
            head.next = pq.poll();
            head = head.next;
        }
        head.next = null;

        return root;
    }
}