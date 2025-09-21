class StockSpanner {
    private int order;
    private Deque<int[]> stack = new ArrayDeque<>();

    public StockSpanner() {
        
    }
    
    public int next(int price) {
        int result = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            int[] prev = stack.pop();
            result = order - prev[1] + prev[2];
        }
        stack.push(new int[]{price, order, result});
        order++;

        return result;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */