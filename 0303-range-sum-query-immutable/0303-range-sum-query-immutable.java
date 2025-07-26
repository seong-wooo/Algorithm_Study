class NumArray {
    int[] n;

    public NumArray(int[] nums) {
        int[] n = new int[nums.length+1];
        for (int i = 0; i <nums.length; i++) {
            n[i+1] = n[i] + nums[i];
        }
        this.n = n;
    }
    
    public int sumRange(int left, int right) {
        return n[right+1] - n[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */