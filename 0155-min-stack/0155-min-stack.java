class MinStack {
    Node head;
    Node tail;
    static class Node {
        Node prev;
        Node next;
        int value;
        int minValue;

        public Node(int value) {
            this.value = value;
        }
    }

    public MinStack() {
        head = new Node(Integer.MAX_VALUE);
        tail = new Node(Integer.MAX_VALUE);
        head.next = tail;
        tail.prev = head;
        head.minValue = Integer.MAX_VALUE;
        tail.minValue = Integer.MAX_VALUE;
    }
    
    public void push(int value) {
        Node newNode = new Node(value);
        Node prev = tail.prev;
        newNode.prev = prev;
        prev.next = newNode;
        newNode.next =tail;
        tail.prev = newNode;
        newNode.minValue = Math.min(value, prev.minValue);
    }
    
    public void pop() {
        Node popNode = tail.prev;
        Node prev = popNode.prev;
        prev.next = tail;
        tail.prev = prev;

        popNode.prev = null;
        popNode.next = null;
    }
    
    public int top() {
        return tail.prev.value;
    }
    
    public int getMin() {
        return tail.prev.minValue;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(value);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */