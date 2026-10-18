class Solution {
    public int calculate(String s) {
        char op = '+';
        int num = 0;
        int result = 0;
        int last = 0;

        for (int i = 0 ; i < s.length(); i++)  { 
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }

            if (!Character.isDigit(c) && c != ' ' || i == s.length() - 1) {
                switch(op) {
                    case('+') -> {result += last; last = num;}
                    case('-') -> {result += last; last = -num; }
                    case('*') -> last *= num;
                    case('/') -> last /= num;
                }
                op = c;
                num = 0;
            }
        }

        return result + last;
    }
}