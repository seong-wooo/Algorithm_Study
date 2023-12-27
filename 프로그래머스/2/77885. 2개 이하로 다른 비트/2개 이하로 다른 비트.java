class Solution {
    public long[] solution(long[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = findBigger(numbers[i]);
        }
        
        return numbers;
    }
    
    public long findBigger(long x) {
        String bx = Long.toBinaryString(x);
        long result = Long.parseLong("10" + bx.substring(1), 2);
        
        for (int i = 0; i < bx.length() - 1; i++) {
            if (bx.charAt(i) == '0') {
                result = (long) Math.min(result, Long.parseLong(bx.substring(0, i) + "10" + bx.substring(i+2), 2));
            }
        }
        
        if (bx.charAt(bx.length() - 1) == '0') {
            result = (long) Math.min(result, Long.parseLong(bx.substring(0, bx.length() - 1) + "1", 2));
        }
        
        return result;
        
    }
}