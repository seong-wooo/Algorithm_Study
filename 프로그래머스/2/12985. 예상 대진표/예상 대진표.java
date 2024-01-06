class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;
        int temp = a + b;
        a = (int) Math.min(a, b);
        b = temp - a;
        a--;
        b--;
        
        while (a / 2 != b / 2) {
            a /= 2;
            b /= 2;
            answer++;
        }
        
        return answer;
    }
}