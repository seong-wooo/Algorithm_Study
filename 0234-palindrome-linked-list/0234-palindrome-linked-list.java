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
    public boolean isPalindrome(ListNode head) {
        Deque<Integer> stack = new LinkedList<>();
        
        while (head != null) {
            stack.add(head.val);
            head = head.next;
        }

        while (!stack.isEmpty()) {
            if (stack.size() <= 1) {
                break;
            }

            if (stack.pollFirst() != stack.pollLast()) {
                return false;
            }
        }
        return true;
    }
}