class Solution {
    public int solution(int[] numbers, int target) {
        return exec(numbers, target, 0);
    }
    
    public int exec(int[] numbers, int target, int index) {
        if (index == numbers.length) {
            return target == 0 ? 1 : 0;
        }
        
        return exec(numbers, target + numbers[index], index + 1) + exec(numbers, target - numbers[index], index + 1);
    }
}