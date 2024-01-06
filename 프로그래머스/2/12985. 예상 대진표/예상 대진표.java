class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;
        int temp = a + b;
        a = (int) Math.min(a, b);
        b = temp - a;
        
        while (a % 2 != 1 || a + 1 != b) {
            a = (a + 1) / 2;
            b = (b + 1) / 2;
            answer++;
        }
        
        return answer;
    }
}