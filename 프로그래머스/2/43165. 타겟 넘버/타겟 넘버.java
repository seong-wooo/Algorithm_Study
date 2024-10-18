class Solution {
    public int solution(int[] numbers, int target) {
        return calc(numbers, 0, target, 0);
    }
    
    public int calc(int[] numbers, int index, int target, int current) {
        if (index == numbers.length) {
            return current == target ? 1 : 0;
        }
        
        return calc(numbers, index + 1, target, current + numbers[index]) + calc(numbers, index + 1, target, current - numbers[index]);
    }
}