class MinStack {
    static class Node {
        int value;
        int minValue;

        Node prev;
        Node next;
        
        public Node(int value, int minValue) {
            this.value = value;
            this.minValue = minValue;
        }
    }

    private final Node head = new Node(0,Integer.MAX_VALUE);
    private final Node tail = new Node(0,0);

    public MinStack() {
        head.next = tail;
        tail.prev = head;
    }
    
    public void push(int value) {
        Node prev = tail.prev;
        int minValue = (int) Math.min(prev.minValue, value);
        Node newNode = new Node(value, minValue);
        prev.next = newNode;
        newNode.prev = prev;
        newNode.next = tail;
        tail.prev = newNode;
    }
    
    public void pop() {
        Node node = tail.prev;
        node.prev.next = tail;
        tail.prev = node.prev;
        node.next = null;
        node.prev = null;
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