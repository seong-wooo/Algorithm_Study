import java.util.*;
import java.util.stream.*;

class Solution {
    public long solution(String expression) {
        long answer = 0;
        
        for (String symbols : List.of("+-*", "+*-", "-+*", "-*+", "*+-", "*-+")) {
            answer = (long) Math.max(Math.abs(calc(expression, symbols, 0)), answer);
        }
        
        return answer;
    }
    
    public long calc(String ex, String symbols, int index) {
        if (index == 3) {
            return Long.parseLong(ex);
        }
        
        String symbol = String.valueOf(symbols.charAt(index));
            
        if (symbol.equals("+")) {
            return Arrays.stream(ex.split("\\" + symbol))
            .mapToLong(x -> calc(x, symbols, index + 1))
            .reduce((a, b) -> a + b).orElse(0);
        }

        if (symbol.equals("-")) {
    
            return Arrays.stream(ex.split(symbol))
            .mapToLong(x -> calc(x, symbols, index + 1))
            .reduce((a, b) -> a - b).orElse(0);
        }
        
        return Arrays.stream(ex.split("\\" + symbol))
        .mapToLong(x -> calc(x, symbols, index + 1))
        .reduce((a, b) -> a * b).orElse(0);
    }
}