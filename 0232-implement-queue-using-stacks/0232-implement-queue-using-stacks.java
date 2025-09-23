class MyQueue {
    Deque<Integer> q1 = new ArrayDeque<>();
    Deque<Integer> q2 = new ArrayDeque<>();

    public MyQueue() {
        
    }
    
    public void push(int x) {
        q1.push(x);
    }
    
    public int pop() {
        if (!q2.isEmpty()) {
            return q2.pop();
        }

        while (!q1.isEmpty()) {
            q2.push(q1.pop());
        }

        return q2.pop();
    }
    
    public int peek() {
     if (!q2.isEmpty()) {
            return q2.peek();
        }

        while (!q1.isEmpty()) {
            q2.push(q1.pop());
        }

        return q2.peek();   
    }
    
    public boolean empty() {
        return q1.isEmpty() && q2.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */